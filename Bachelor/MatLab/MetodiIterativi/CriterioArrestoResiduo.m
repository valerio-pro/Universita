function decisioneBooleana = CriterioArrestoResiduo(residuo, b, epsilon)
    
    % La seguente funzione implementa il criterio di arresto del residuo,
    % prende in input un certo vettore "residuo", il termine noto "b" e la 
    % soglia di precisione "epsilon". Restituisce "true" se i parametri di input
    % soddisfano il criterio di arresto del residuo, "false" altrimenti.
    
    % Si calcolano le norme 2 del vettore "residuo" e del termine noto "b"
    norma2Residuo = norm(residuo, 2);
    norma2b = norm(b, 2);
   

    % Si verifica se e' soddisfatto il criterio di arresto
    if norma2Residuo <= epsilon*norma2b
        decisioneBooleana = true;
    else
        decisioneBooleana = false;
    end

end