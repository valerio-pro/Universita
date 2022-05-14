function number = RuffiniHorner(Nodi, Valori, t)
    
    % La seguente funzione, dato il vettore dei nodi "Nodi" e il vettore dei valori "Valori",
    % valuta il polinomio di interpolazione in uno specifico punto "t" di input, 
    % utilizzando il metodo di Ruffini-Horner.
    
    % Questa funzione non prende in input il vettore delle differenze 
    % divise.
 
 
    vettore = CalcolaVettoreDifferenzeDivise(Nodi, Valori);

    n = length(Nodi);
    h = zeros(1, n);

    % Si calcolano i vari valori "h_n", ..., "h_1"
    % Attenzione: il vettore "h" usa l'indicizzazione al contrario, cioe' in
    % h(1) si trovera' f[x_1, ..., x_n] e in h(n) si trovera' p(t), quindi
    % la funzione restituisce il valore h(n) che sarebbe proprio p(t)
    h(1) = vettore(n);
    for k = 2:n
        h(k) = vettore(n-k+1) + ( h(k-1) * (t - Nodi(n-k+1)) );
    end

    number = h(n);

end
