function [vettoreCalcolato, indiceIterazione, norma2Residuo] = MetodoJacobiRilassato(A, b, w, epsilon, vettoreInnesco, Nmax)
    
    % La seguente funzione implementa il metodo iterativo di Jacobi con rilassamento.

    % In input viene presa la matrice "A", il termine noto "b", un parametro di
    % rilassamento "w", la soglia di precisione "epsilon", il vettore di innesco
    % "vettoreInnesco" e il massimo numero di iterazioni eseguibili "Nmax".
    
    % In output e' restituito "vettoreCalcolato", cioe' il primo vettore che
    % soddisfa il criterio di arresto del residuo, "indiceIterazione" che e'
    % l'indice dell'ultima iterazione eseguita e "norma2Residuo" che e' la
    % norma 2 dell'ultimo vettore residuo. Se viene raggiunto il massimo
    % numero di iterazioni allora vengono restituiti gli stessi parametri ma
    % relativamente all'iterazione di indice "Nmax" (per essere
    % arrivati all'iterazione "Nmax" nessun vettore calcolato ha soddisfatto il 
    % criterio di arresto del residuo).
    
    % Si assume che la matrice "A" sia quadrata e che abbia elementi diagonali 
    % non nulli. Si assume che il parametro di rilassamento "w" sia diverso da
    % 0. Si assume che "Nmax" sia almeno pari a 1.
    
    % Esempio da eseguire in command line:
    % [vettore, indice, normaResiduo] = MetodoJacobiRilassato([2,1;1,2], [1;1], 0.5, 0.00000001, [0;0], 28)

    
    % La matrice precondizionatore del metodo e' ottenuta come la matrice
    % che ha sulla diagonale gli stessi elementi sulla diagonale di "A" 
    % moltiplicati per "1/w" e ha 0 in tutte le altre entrate
    D = (1/w)*diag(diag(A));
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
        % l'operazione "D\residuoCorrente" restituisce il vettore soluzione
        % "z" del sistema lineare "Dz = residuoCorrente"
        vettoreCorrente = vettoreCorrente + D\residuoCorrente;

    end
    
    % Nessun vettore della successione generata ha soddisfatto il criterio
    % di arresto del residuo. Si restituiscono i dati calcolati durante
    % l'ultima iterazione
    indiceIterazione = Nmax;
    norma2Residuo = norm(residuoCorrente, 2);
    vettoreCalcolato = vettoreCorrente;

end
