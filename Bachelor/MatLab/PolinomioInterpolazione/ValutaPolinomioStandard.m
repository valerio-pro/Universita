function number = ValutaPolinomioStandard(Nodi, Vettore, t)
    
    % La seguente funziona valuta il polinomio di interpolazione in uno
    % specifico punto "t" di input, utilizzando il metodo di calcolo standard.
    % In input e' fornito anche il vettore delle differenze divise dei nodi
    % x_1, ..., x_n

    n = length(Nodi);

    % vettoreProdotti conterra' gli elementi (t - x_1), ..., (t - x_n)
    vettoreProdotti = zeros(1, n);
    
    tmp = 1;
    for k = 1:n
        vettoreProdotti(k) = tmp;
        tmp = tmp*(t - Nodi(k));
    end
    
    number = 0;
    for k = 1:n
        number = number + (Vettore(k)*vettoreProdotti(k));
    end

end
