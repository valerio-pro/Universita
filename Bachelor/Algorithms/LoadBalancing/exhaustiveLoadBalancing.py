import queue
from functools import reduce
import ProblemaLoadBalancing as PLB 


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
        return soluzioneGreedy


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
        # analizzare molti meno sottoproblemi
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
    
    # Viene ritornata la coppia "(caricoPiuGrandeOttenuto, assegnazioneAlleMacchine)"
    return best



# Algoritmo greedy (3/2)-approssimante per Load Balancing
def greedyLoadBalancing(fileName):
    
    # Lettura dell'input
    (n, m, tempiEsecuzione) = readFromInputFile(fileName)

    # Vengono ordinati i task in senso non crescente di tempo di esecuzione.
    # Lo stesso algoritmo ma senza questo ordinamento iniziale sarebbe stato 2-approssimante
    tempiEsecuzione.sort(reverse = True)

    # Ho scelto di modellare l'output come un dizionario che associa ad ogni macchina
    # la lista dei tempi di esecuzione ad essa assegnati
    assegnazione = {}

    # Viene utilizzata una coda con priorita' ottenuta dal modulo "queue", 
    # le macchine vengono inserite nella coda come tuple "(Priorita', Macchina)",
    # la priorita' di una macchina e' data dalla somma dei tempi di esecuzione
    # dei task ad essa assegnati 
    codaCarichi = queue.PriorityQueue()
    for i in range(1, m+1):
        assegnazione[i] = []
        codaCarichi.put( (0, i) )

    # Iterazione sugli "n" task
    for i in range(1, n+1):
        
        toBeScheduled = tempiEsecuzione[i-1]

        # Seleziona la macchina con carico minimo, il metodo "get()" estrae di default l'item con valore minimo associato
        (carico, macchina) = codaCarichi.get()
        assegnazione[macchina].append(toBeScheduled)
        
        carico += toBeScheduled
        codaCarichi.put( (carico, macchina) )

    # Viene ritornata una tupla "(caricoPiuGrandeOttenuto, assegnazioneAlleMacchine)"
    return ( (lambda x: max([reduce(lambda y,z: y+z, value) for value in list(x.values()) if len(value) > 0])) (assegnazione), assegnazione )


# Funzione main
def main():
    
    soluzione = exhaustiveLoadBalancing('input.txt')
    print(soluzione)
    

if __name__ == '__main__':
    main()
