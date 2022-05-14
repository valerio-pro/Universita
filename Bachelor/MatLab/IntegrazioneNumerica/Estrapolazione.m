function valoreEstrapolato = Estrapolazione(a, b, funzione, vettore)
    
    % Questa funzione implementa il metodo di estrapolazione per il calcolo
    % approssimato dell'integrale della funzione di input sull'intervallo di
    % input "[a,b]". Prende in input anche "m" numeri n_1, ..., n_m che saranno
    % usati per il calcolo di I_(n_1), ..., I_(n_m)
    
    % Si assume "b" >= "a"
    % Si assume la funzione di input sia definita su "[a,b]"
    % Si assume n_1, ..., n_m siano tutti distinti
    % Si assume n_1, ..., n_m >= 1

    m = length(vettore);
    vettoreDeiPassi = zeros(1, m);
    
    % Si calcola il vettore dei passi (al quadrato), in posizione "k" del 
    % vettore ci sara' (h_k)^2 dove h_k = (b-a)/n_k 
    for k = 1:m
        vettoreDeiPassi(k) = ( (b - a)/(vettore(k)) )^2;
    end

    vettoreFormuleDeiTrapezi = zeros(1, m);
    for k = 1:m
        vettoreFormuleDeiTrapezi(k) = FormulaDeiTrapezi(a, b, vettore(k), funzione);
    end
    
    % Si valuta il polinomio di interpolazione dei dati 
    % ( (h_1)^2, I_(n_1) ), ..., ( (h_m)^2, I_(n_m) ) utilizzando il metodo
    % Ruffini-Horner. 
    valoreEstrapolato = RuffiniHorner(vettoreDeiPassi, vettoreFormuleDeiTrapezi, 0);

end
