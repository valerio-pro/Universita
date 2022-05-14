function approssimazione = FormulaDeiTrapezi(a, b, n, funzione)
    
    % La funzione prende in input gli estremi di un intervallo "[a,b]", il numero
    % "n" di intervallini in cui verra' suddiviso "[a,b]" e una funzione definita
    % su "[a,b]". La funzione restituisce in output l'approssimazione, calcolata 
    % attraverso la formula dei trapezi di ordine "n", dell'integrale della 
    % funzione di input sull'intervallo "[a,b]"
    
    % Si assume "b" >= "a"
    % Si assume "n" >= 1
    % Si assume che la funzione di input sia definita su "[a,b]"

    passo = (b - a)/n;
    vettoreXj = zeros(1, n);
    
    % Si calcola il vettore di tutti i punti x_j, escluso x_0 (cioe' "a") e 
    % x_n (cioe' "b")
    for j = 1:n-1
        vettoreXj(j) = a + (j * passo);
    end
    
    % Si calcola il primo termine della formula dei trapezi
    termine1 = (funzione(a) + funzione(b))/2;
    
    % Si calcola il secondo termine della formula dei trapezi
    termine2 = 0;
    for k = 1:n-1
        termine2 = termine2 + funzione(vettoreXj(k));
    end

    approssimazione = passo * (termine1 + termine2);

end
