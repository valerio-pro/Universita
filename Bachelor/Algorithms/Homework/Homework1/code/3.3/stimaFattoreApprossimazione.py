import queue
from functools import reduce
from numpy.random import randint
import ProblemaLoadBalancing as PLB

# Posizionarsi nella directory del file system che contiene lo script 
def readFromInputFile(fileName):

    with open(fileName, 'r') as inputFile:
        righe = [riga.strip() for riga in inputFile]
        firstLineList = righe[0].split(' ')
        n, m = int(firstLineList[0]), int(firstLineList[1]) 
        tempiEsecuzione = [int(i) for i in righe[1:] if i != '']

    return (n, m, tempiEsecuzione)


# Funzione per generare una istanza casuale di Load Balancing. La funzione "randint()" della libreria numpy.random consente di generare 
# un numero intero nell'intervallo [low, high) con probabilita' uniforme. Viene scritto il file "input.txt" con i valori generati
def generaIstanzaLoadBalancing():

    # Ho lasciato impostato "m = 2" e "n = 5" fissati
    m = randint(low = 2, high = 3)
    n = randint(low = 5, high = 6)

    # Si ottengono "n" taskTime generati dall'intervallo [1, 250]
    tempiEsecuzione = list(randint(low = 1, high = 251, size = n))

    # Si scrive il file "input.txt" con i parametri appena generati, il file verra' poi preso in input dall'algoritmo esaustivo
    with open('input.txt', 'w') as inputFile:
        inputFile.write(str(n) + ' ' + str(m) + '\n')
        for i in tempiEsecuzione:
            inputFile.write(str(i) + '\n')
    


# Funzione per calcolare la media di "t" rapporti di approssimazione restituiti da "exhaustiveLoadBalancing"
# Ho lasciato "t" impostato a 50 iterazioni
def stimaFattoreApprossimazione(t = 50):

    # Il fattore di approssimazione e' inizializzato a 0
    fattoreApprossimazione = 0

    for _ in range(t):
        generaIstanzaLoadBalancing()
        fattoreApprossimazione += exhaustiveLoadBalancing('input.txt')
        # print(fattoreApprossimazione)

    return fattoreApprossimazione/t



# Algoritmo greedy per Load Balancing
def greedyLoadBalancing(fileName):
    
    # Lettura dell'input
    (n, m, tempiEsecuzione) = readFromInputFile(fileName)
    
    # Vengono ordinati i task in senso non crescente di tempo di esecuzione
    tempiEsecuzione.sort(reverse = True)

    # Ho scelto di modellare l'output come un dizionario che associa ad ogni macchina
    # la lista dei tempi di esecuzione ad essa assegnati
    assegnazione = {}

    # Viene utilizzata una coda con priorita' ottenuta dal modulo "queue", 
    # le macchine vengono inserite nella coda come tuple "(Priorita', Macchina)",
    # la priorita' di una macchina e' data dalla somma dei tempi di esecuzione
    # dei task ad essa assegnati. Inizialmente ogni macchina avra' carico (quindi priorita') pari a 0
    codaCarichi = queue.PriorityQueue()
    for i in range(1, m+1):
        assegnazione[i] = []
        codaCarichi.put( (0, i) )

    # Iterazione sugli "n" task
    for i in range(1, n+1):
        
        toBeScheduled = tempiEsecuzione[i-1]

        # Seleziona la macchina con carico minimo e assegna a tale macchina l'i-esimo task, 
        # il metodo "get()" estrae di default l'item con priorita' minima
        (carico, macchina) = codaCarichi.get()
        assegnazione[macchina].append(toBeScheduled)
        
        carico += toBeScheduled
        codaCarichi.put( (carico, macchina) )

    # Viene ritornata una tupla "(caricoPiuGrandeOttenuto, assegnazione)"
    return ( (lambda x: max([reduce(lambda y,z: y+z, value) for value in list(x.values()) if len(value) > 0])) (assegnazione), assegnazione )



# Algoritmo di Ricerca Esaustiva Intelligente (tecnica Branch-And-Bound) per Load Balancing
def exhaustiveLoadBalancing(fileName):

    # Lettura dell'input
    (n, m, tempiEsecuzione) = readFromInputFile(fileName)
    
    # Si determina subito la soluzione greedy e la si usa come best iniziale, la variabile "best" sara' 
    # quindi una coppia "(caricoPiuGrande, assegnazioneCompletaCorrente)"
    soluzioneGreedy = greedyLoadBalancing(fileName)
    best = soluzioneGreedy

    # Se ci sono piu' macchine che task oppure se c'e' solo una macchina, allora greedy trova sempre la soluzione ottima
    if m >= n or m == 1:
        return 1.0


    # L'insieme dei sottoproblemi e' implementato come una coda che segue una politica LIFO. Spesso tale politica consente di trovare
    # piu' in fretta delle soluzioni complete, quindi puo' portare a scartare piu' sottoproblemi
    S = queue.LifoQueue()

    # Il problema iniziale ha due caratteristiche principali:
    #   - ad ogni macchina e' associata una lista vuota di tempi di esecuzione dei task schedulati (dizionario "assegnazioneTask") 
    #   - devono ancora essere schedulati tutti i task (dizionario "taskRimanenti")
    ProblemaIniziale = PLB.Problema(m = m, assegnazioneTask = {i:[] for i in range(1, m+1)}, taskRimanenti = {i:tempiEsecuzione[i-1] for i in range(1, n+1)})
    S.put(ProblemaIniziale)

    while not S.empty():
        
        # Si estrae un problema da "S"
        Problema = S.get()

        taskRimanentiProblema = Problema.getTaskRimanenti()

        # Per ogni task (del problema corrente appena estratto) che deve essere ancora schedulato si generano "m" sottoproblemi,
        # il sottoproblema i-esimo cosi' generato (in posizione "i-1" della lista "sottoProblemi" ) avra' il task "task" 
        # assegnato alla macchina i-esima
        #
        # Osservazione: se in "taskRimanentiProblema" ci sono task diversi ma con stessi tempi di esecuzione allora verranno a crearsi 
        # piu' sottoproblemi in un certo senso "identici", non sono riuscito ad ottimizzare questo dettaglio che avrebbe consentito di 
        # analizzare meno sottoproblemi
        for task in taskRimanentiProblema:
                
            sottoProblemi = Problema.espandiProblema(task)
    
            if sottoProblemi:

                for sottoProblema in sottoProblemi:
                    
                    # Se il problema corrente costituisce una soluzione completa e tale soluzione e' migliore di "best[0]" (che contiene
                    # il carico corrente piu' grande tra le macchine) allora si aggiorna "best"
                    if PLB.Problema.checkSoluzioneCompleta(sottoProblema):
                        if sottoProblema.getCaricoPiuGrande() < best[0]:
                            best = (sottoProblema.getCaricoPiuGrande(), sottoProblema.getAssegnazioneTask())
                        
                    # Se la soluzione non e' completa e il lower bound associato non supera il best corrente allora si aggiunge il 
                    # sottoproblema alla coda dei sottoproblemi
                    elif sottoProblema.lowerBound() < best[0]:
                        S.put(sottoProblema)

        del Problema
    
    # Viene ritornato il rapporto tra il costo della soluzione greedy e il costo della soluzione ottima
    return soluzioneGreedy[0]/best[0]


# Funzione main
def main():
    
    mediaRapportiApprossimazione = stimaFattoreApprossimazione()
    print(mediaRapportiApprossimazione)
    

if __name__ == '__main__':
    main()