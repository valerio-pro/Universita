function vettoreDiValutazione = ValutaPolinomioInPiuPunti(Nodi, Valori, T)
    
    % La seguente funzione prende in input tre vettori: "Nodi", "Valori",
    % "T"
    % "Nodi" e' il vettore dei nodi di interpolazione x_1, ..., x_n
    % "Valori" e' il vettore dei valori y_1, ..., y_n
    % "T" e' il vettore degli "m" punti in cui si vuole valutare il polinomio
    
    % La funzione restituisce il vettore "[p(t_1), ..., p(t_m)]", utilizzando per
    % il calcolo di ciascun "p(t_i)" il metodo di Ruffini-Horner
    
    % Si assume che tutti i nodi siano distinti
    % Si assume che il vettore "Nodi" e il vettore "Valori" abbiano stessa
    % lunghezza

    vettoreDifferenzeDivise = CalcolaVettoreDifferenzeDivise(Nodi, Valori);
    m = length(T);
    
    vettoreDiValutazione = zeros(1, m);
    for k = 1:m
        vettoreDiValutazione(k) = ValutaPolinomioRuffiniHorner(Nodi, vettoreDifferenzeDivise, T(k));
    end

end
