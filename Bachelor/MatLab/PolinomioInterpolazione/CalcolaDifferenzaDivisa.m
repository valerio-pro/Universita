function number = CalcolaDifferenzaDivisa(Nodi, Valori)
    
    % La seguente funzione calcola la differenza divisa "f[x_0,...,x_n]"
    % dati in input il vettore "Nodi" [x_0,...,x_n] e il vettore "Valori"
    % [f(x_0),...,f(x_n)].

    % Si assume che il vettore "Nodi" e "Valori" abbiano stessa lunghezza


    % Si calcola la lunghezza del vettore di Nodi
    n = length(Nodi);

    if n == 1

        % Se il vettore ha solo un elemento allora ci troviamo nel caso
        % base del calcolo della differenza divisa
        number = Valori(n);
        return 

    end
    
    % Si calcola f[x_0, x_1, ..., x_k-2, x_k]
    differenzaDivisa1 = CalcolaDifferenzaDivisa([Nodi(1:n-2), Nodi(n:n)], [Valori(1:n-2), Valori(n:n)]);
    
    % Si calcola f[x_0, x_1, ..., x_k-2, x_k-1]
    differenzaDivisa2 = CalcolaDifferenzaDivisa(Nodi(1:n-1), Valori(1:n-1));
    
    % Si calcola la differenza x_k - x_k-1
    diff = Nodi(n) - Nodi(n-1);
    
    number = (differenzaDivisa1 - differenzaDivisa2)/diff;

end