function [vettoreCalcolato, indiceIterazione, norma2Residuo] = MetodoGaussSeidel(A, b, epsilon, vettoreInnesco, Nmax)
    
    % La seguente funzione implementa il metodo iterativo di Gauss-Seidel.

    % In input viene presa la matrice "A", il termine noto "b", la soglia di
    % precisione "epsilon", il vettore di innesco "vettoreInnesco" e il massimo
    % numero di iterazioni eseguibili "Nmax".
    
    % In output e' restituito "vettoreCalcolato", cioe' il primo vettore che
    % soddisfa il criterio di arresto del residuo, "indiceIterazione" che e'
    % l'indice dell'ultima iterazione eseguita e "norma2Residuo" che e' la
    % norma 2 dell'ultimo vettore residuo. Se viene raggiunto il massimo
    % numero di iterazioni allora vengono restituiti gli stessi parametri ma
    % relativamente all'iterazione di indice "Nmax" (per essere
    % arrivati all'iterazione "Nmax" nessun vettore calcolato ha soddisfatto il 
    % criterio di arresto del residuo).
    
    % Si assume che la matrice "A" sia quadrata e che abbia elementi diagonali 
    % non nulli. Si assume che "Nmax" sia almeno pari a 1.
    
    % Esempio da eseguire in command line:
    % [vettore, indice, normaResiduo] = MetodoGaussSeidel([2,1;1,2], [1;1], 0.00000001, [0;0], 28)

    
    % La matrice precondizionatore del metodo e' ottenuta come la porzione
    % triangolare inferiore di "A", ha 0 in tutte le restanti entrate
    E = tril(A);
    vettoreCorrente = vettoreInnesco;

    for k = 1:Nmax
        
        % Come primo passo di ogni iterazione si calcola il residuo della 
        % soluzione approssimata corrente e si verifica se il criterio di
        % arresto e' soddisfatto. Alla prima iterazione si effettuano tali
        % calcoli per il vettore di innesco
        residuoCorrente = b - A*vettoreCorrente;
        decisioneArresto = CriterioArrestoResiduo(residuoCorrente, b, epsilon);
        
        % Se il criterio di arresto del residuo e' soddisfatto allora e'
        % possibile terminare il programma 
        if decisioneArresto == true

            vettoreCalcolato = vettoreCorrente;
            norma2Residuo = norm(residuoCorrente, 2);
            indiceIterazione = k;

            % Se nella prima iterazione (k = 1), prima di calcolare il
            % primo vettore della successione, abbiamo che il criterio di
            % arresto del residuo e' soddisfatto allora significa che il
            % vettore di innesco e' gia' una buona approssimazione della
            % soluzione del sistema lineare e dunque l'indice
            % dell'iterazione ritornato e' 0
            if k == 1
                indiceIterazione = 0;
            end

            return

        end
        
        % Si calcola il prossimo vettore della successione (il k-esimo)
        % l'operazione "E\residuoCorrente" restituisce il vettore soluzione
        % "z" del sistema lineare "Ez = residuoCorrente"
        vettoreCorrente = vettoreCorrente + E\residuoCorrente;

    end
    
    % Nessun vettore della successione generata ha soddisfatto il criterio
    % di arresto del residuo. Si restituiscono i dati calcolati durante
    % l'ultima iterazione
    indiceIterazione = Nmax;
    norma2Residuo = norm(residuoCorrente, 2);
    vettoreCalcolato = vettoreCorrente;

end
