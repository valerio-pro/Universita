import queue
from functools import reduce

# Posizionarsi nella directory del file system che contiene sia lo script che il file 'input.txt'
# Il file di input contiene nella prima riga due interi "n" ed "m" separati da uno spazio che indicano rispettivamente
# il numero di task da schedulare e il numero di macchine a disposizione. Le successive "n" righe indicano i tempi di esecuzione
# dei task da schedulare
def readFromInputFile(fileName):

    with open(fileName, 'r') as inputFile:
        righe = [riga.strip() for riga in inputFile]
        firstLineList = righe[0].split(' ')
        n, m = int(firstLineList[0]), int(firstLineList[1]) 
        tempiEsecuzione = [int(i) for i in righe[1:] if i != '']

    return (n, m, tempiEsecuzione)



# Posizionarsi nella directory del file system in cui e' presente lo script per avere il file "output.txt" creato nella
# stessa directory.
# Il file di output conterra' un solo intero rappresentante il carico piu' grande assegnato alle macchine
def writeOnOutputFile(soluzione):

    # Viene scritto nel file "output.txt" il costo della soluzione trovata (il carico piu' grande)
    with open('output.txt', 'w') as outputFile:
        outputFile.write(str(soluzione))



# Algoritmo greedy (3/2)-approssimante per Load Balancing
def greedyLoadBalancing(fileName):
    
    # Lettura dell'input
    (n, m, tempiEsecuzione) = readFromInputFile(fileName)

    # Vengono ordinati i task in senso non crescente di tempo di esecuzione.
    # Lo stesso algoritmo ma senza questo ordinamento iniziale sarebbe stato 2-approssimante
    tempiEsecuzione.sort(reverse = True)
    
    # Ho scelto di modellare l'output come un dizionario che associa ad ogni macchina
    # la lista dei job ad essa assegnati, prima del return viene comunque effettuata la scrittura
    # su file del carico piu' grande ottenuto
    assegnazione = {}

    # Viene utilizzata una coda con priorita' ottenuta dal modulo "queue", 
    # le macchine vengono inserite nella coda come tuple "(Priorita', Macchina)",
    # dove la priorita' di una macchina e' data dalla somma dei tempi di esecuzione
    # dei task ad essa assegnati. Inizialmente ogni macchina avra' carico (quindi priorita') pari a 0
    codaCarichi = queue.PriorityQueue()
    for i in range(1, m+1):
        assegnazione[i] = []
        codaCarichi.put( (0, i) )

    # Iterazione sugli "n" task
    for i in range(1, n+1):

        toBeScheduled = tempiEsecuzione[i-1]

        # Seleziona la macchina con carico minimo e assegna a tale macchina l'i-esimo task, 
        # il metodo "get()" estrae di default l'item con valore minimo associato
        (carico, macchina) = codaCarichi.get()
        assegnazione[macchina].append(toBeScheduled)
        
        carico += toBeScheduled
        codaCarichi.put( (carico, macchina) )


    # "soluzione" e' una tupla "(caricoPiuGrandeOttenuto, assegnazioneAlleMacchine)"
    soluzione = ( (lambda x: max([reduce(lambda y,z: y+z, value) for value in list(x.values())])) (assegnazione), assegnazione )

    # Si scrive sul file di output il carico piu' grande ottenuto dall'algoritmo greedy
    writeOnOutputFile(soluzione[0])

    # Viene ritornata la tupla "soluzione"
    return soluzione


# Funzione main
def main():
    
    soluzione = greedyLoadBalancing('input.txt')
    print(soluzione)
    

if __name__ == '__main__':
    main()
