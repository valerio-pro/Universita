from numpy.random import random
# import matplotlib.pyplot as plt


# Funzione per la scrittura su file di output
def writeResultsOnFile(stopList):

    with open('output.txt', 'w') as outFile:

        for i in range(len(stopList)):
            outFile.write(str(stopList[i]) + '\n')


# Funzione di lettura dell'input, assicurarsi di essere posizionati nel file system nella directory che contiene sia script che file di input
def readLineFromFile(filename):

    with open(filename, 'r') as inFile:

        line = [riga.strip() for riga in inFile]
        firstLine = line[0].split(' ')
        n, t = int(firstLine[0]), int(firstLine[1]) 

    return n, t 



'''
# Funzione per mostrare come si distribuiscono i valori della "stopList" sui nodi da 1 a "n" (nodo 0 escluso)
def makePlot(stopList):

    plt.figure(figsize=(12, 6))

    numbers = [i for i in range(1, len(stopList)+1)]

    # Otteniamo diverse "stopList" al variare di "n"
    stopList2 = simulazione(n = 5, t = 10**5)
    stopList3 = simulazione(n = 10, t = 10**5)
    stopList4 = simulazione(n = 15, t = 10**5)
    

    numbers2 = [i for i in range(1, len(stopList2)+1)]
    numbers3 = [i for i in range(1, len(stopList3)+1)]
    numbers4 = [i for i in range(1, len(stopList4)+1)]
    

    (linea1,) = plt.plot(numbers, stopList, 'b')
    (linea2,) = plt.plot(numbers2, stopList2, 'r')
    (linea3,) = plt.plot(numbers3, stopList3, 'g')
    (linea4,) = plt.plot(numbers4, stopList4, 'y')
    

    # plt.legend([linea1], [f'n = {len(numbers)}, p = {0.5}, t = {10**5}'])

    plt.legend([linea1,linea2,linea3,linea4], [f'n = {len(numbers)}, p = {0.5}, t = {10**5}',
                                                f'n = {len(numbers2)}, p = {0.5}, t = {10**5}',
                                                f'n = {len(numbers3)}, p = {0.5}, t = {10**5}',
                                                f'n = {len(numbers4)}, p = {0.5}, t = {10**5}'])
    

    plt.xticks(ticks = [1, 5, 10, 15, 20], labels = [1, 5, 10, 15, 20])
    plt.xlabel('Etichetta Nodi')
    plt.ylabel('Numero di Stop')
    
    plt.show()
'''


# Funzione di simulazione
def simulazione(n, t):

    # La lista "stopList" conta il numero delle volte che la pedina si ferma su un nodo dell'anello. La posizione "i-esima" della lista contiene un intero
    # che e' il numero di volte che la pedina si e' fermata sul nodo "i". La pedina parte dal nodo 0 e non si ferma mai su di esso, 
    # quindi la posizione 0 della lista contiene 0
    stopList = [0 for _ in range(0, n+1)]

    # Simulazioni del processo e aggiornamento della "stopList"
    for _ in range(t):
        nodo = pedina(n)
        stopList[nodo] += 1

    return stopList[1:]


# Funzione della pedina
def pedina(n):

    # Lista dei nodi visitati dalla pedina, inizialmente si trova sul nodo 0
    visited = [0]

    # La variabile "posPedina" tiene conto della posizione corrente della pedina
    posPedina = 0

    # Finche' non abbiamo visitato tutti i nodi spostiamo la pedina
    while len(visited) != n+1:

        # Si sceglie un numero u.a.r. in [0,1]
        p = random()

        # Movimento orario
        if p <= 0.5:

            posPedina = (posPedina + 1) % (n+1)

        # Movimento antiorario
        else:

            posPedina = (posPedina - 1) % (n+1)

        # Se la pedina e' in un nodo nuovo allora lo si aggiunge alla lista dei nodi visitati
        if posPedina not in visited:
            visited.append(posPedina)

    return posPedina



# Funzione main
def main():

    # Lettura dei parametri di input
    n, t = readLineFromFile('input.txt')

    # Esecuzione della funzione di simulazione
    stopList = simulazione(n, t)

    # Viene passata la "stopList" alla funzione per la scrittura dell'output su file
    writeResultsOnFile(stopList)

    print(f'Numero di nodi: {n}\nLista di stop della pedina sui nodi: {stopList}')

    # makePlot(stopList)


if __name__ == '__main__':
    main()