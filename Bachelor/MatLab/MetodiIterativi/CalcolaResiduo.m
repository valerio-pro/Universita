function vettoreResiduo = CalcolaResiduo(A, b, vettore)
    
    % La seguente funzione calcola il vettore residuo di un sistema lineare
    % data in input la matrice "A" del sistema, il termine noto "b" e il
    % vettore della soluzione approssimata "vettore". 

    vettoreResiduo = b - A*vettore;

end