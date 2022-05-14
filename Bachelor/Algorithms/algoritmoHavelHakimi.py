# L'algoritmo di Havel-Hakimi decide se, data una sequenza degs[1:n] di "n" interi, esiste un grafo semplice di "n" vertici in cui i vertici hanno
# come grado gli interi della sequenza, cioe' degs[i] = grado(v_i) per ogni i = 1,...,n

# Osservazione 1: una sequenza di gradi dove ogni grado e' pari a 0 e' una sequenza che soddisfa il predicato del problema (nodi scollegati)
# Osservazione 2: dato che la somma dei gradi dei nodi deve essere pari a 2 volte il numero di archi, deve risultare che la somma dei gradi dati in input sia un numero pari
# Osservazione 3: per ogni i = 1,...,n deve risultare 0 <= degs[i] <= n-1

# Principio dell'algoritmo: ordina i gradi in ordine decrescente e verifica se la somma e' un numero pari, poi chiama una procedura
# ricorsiva dove ad ogni passo controlla se la sequenza e' fatta tutta da 0, poi estrae l'intero in testa alla sequenza che vale "K" e 
# sottrae 1 ai successivi "K" interi della sequenza 


# Questa implementazione ha costo O((n^2)*(log(n))), perche' ho al piu' "n" chiamate ricorsive e in ogni chiamata ricorsiva bisogna 
# riordinare al piu' "n" elementi (costo per riordinare -> O(n*log(n)))
def Havel_Hakimi(degs):

    n = len(degs)

    # grafo vuoto
    if n == 0:
        return True

    # somma dei gradi deve essere pari
    if not ((sum(degs)%2) == 0):
        return False

    # controllo sul range dei valori dei gradi
    for i in degs:
        if i >= n or i < 0:
            return False

    degs.sort(reverse = True)
    return Havel_Hakimi_Recursive(degs)


def Havel_Hakimi_Recursive(degs):
    cnt = 0
    
    # se ho tutti 0 nella lista dei gradi allora esiste un grafo semplice che soddisfa la proprieta'
    for i in degs:
        if i == 0:
            cnt += 1
        if i < 0:
            return False
    
    if cnt == len(degs):
        return True

    # riordinare e' necessario
    degs.sort(reverse = True)
    # print(degs)
    
    d = degs.pop(0)
    
    for i in range(0, d):
        degs[i] -= 1
    
    return Havel_Hakimi_Recursive(degs)

def main():
    degs = [2, 2, 2, 3, 1]
    decision = Havel_Hakimi(degs)
    print(decision)


if __name__ == '__main__':
    main()
