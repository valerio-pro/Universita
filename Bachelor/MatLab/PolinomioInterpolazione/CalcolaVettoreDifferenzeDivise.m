function vettore = CalcolaVettoreDifferenzeDivise(Nodi, Valori)
    
    % La seguente funzione, dati i nodi di interpolazione x_1, ..., x_n e i
    % valori y_1, ..., y_n, calcola la tabella delle differenze divise 
    % e restituisce il vettore diagonale di tale tabella
    
    n = length(Nodi);
    tabella = zeros(n);
    
    % Si calcola la prima colonna della tabella delle differenze divise
    for i = 1:n
        tabella(i,1) = Valori(i);
    end

    % Con l'indice "i" si scandiscono le righe della tabella delle
    % differenze divise, con la "j" si scandiscono le colonne della tabella
    % delle differenze divise.

    for j = 2:n
        for i = 2:n
            % Controllo per rimanere a calcolare valori al di sotto della diagonale
            if j <= i
                tabella(i,j) = ((tabella(i,j-1)-tabella(j-1,j-1))/(Nodi(i)-Nodi(j-1)));
            end
        end
    end
   
    % Si trova il vettore diagonale della tabella delle differenze divise
    vettore = zeros(1, n);
    for k = 1:n
        vettore(k) = tabella(k,k);
    end

end
