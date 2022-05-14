function number = ValutaPolinomioRuffiniHorner(Nodi, Vettore, t)
    
    % La seguente funzione valuta il polinomio di interpolazione in uno
    % specifico punto "t" di input, utilizzando il metodo di Ruffini-Horner.
    % In input e' fornito anche il vettore delle differenze divise dei nodi
    % x_1, ..., x_n dato che questa procedura potrebbe essere utilizzata piu'
    % volte e non avrebbe senso stare a calcolare piu' volte il vettore delle
    % differenze divise (il vettore non cambia).

    n = length(Nodi);
    h = zeros(1, n);

    % Si calcolano i vari valori h_n, ..., h_1
    % Attenzione: il vettore "h" usa l'indicizzazione al contrario, cioe' in
    % h(1) si trovera' f[x_1, ..., x_n] e in h(n) si trovera' "p(t)", quindi
    % la funzione restituisce il valore "h(n)" che sarebbe proprio "p(t)"
    h(1) = Vettore(n);
    for k = 2:n
        h(k) = Vettore(n-k+1) + ( h(k-1) * (t - Nodi(n-k+1)) );
    end

    number = h(n);

end
