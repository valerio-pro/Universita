import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt
import queue
import ProblemaVertexCover as ProblemaVC

# La prima riga del file conterra' il numero di elementi del vertex cover
# Le successive len(VertexCover) righe conterranno tutti i vertici del vertex cover trovato
# Attenzione alla directory in cui viene salvato il file
def writeResultsOnFile(number, VertexCover):
    with open('risultatiExhaustiveVertexCover.txt', 'w') as outFile:
        outFile.write(str(number) + '\n')
        if number > 0:
            for i in VertexCover:
                outFile.write(str(i) + '\n')


# Algoritmo di Ricerca Esaustiva Intelligente (tecnica Branch-And-Bound) per MinVertexCover
def exhaustiveVertexCover(G):

    # Se il grafo e' completamente sconnesso allora non bisogna coprire gli archi
    if len(G.edges) == 0:
        return (0, set())

    Gtmp = G.copy()
    
    # Un "problema" e' modellato come un grafo e un insieme di vertici che rappresenta il vertex cover che si sta costruendo
    ProblemaIniziale = ProblemaVC.Problema(Grafo = Gtmp, vertici = set())

    # Il valore "best" iniziale e' dato dall'insieme dei nodi del grafo di input
    best = (len(G.nodes), set(G.nodes))
    
    S = queue.LifoQueue()
    S.put(ProblemaIniziale)
    while not S.empty():

        # La coda dei sottoproblemi segue una politica LIFO
        Problema = S.get()
        nodiProblemaCorrente = list(Problema.Grafo.nodes)
        
        for i in nodiProblemaCorrente:

            # Il sottoproblema e' ottenuto dal problema corrente, rimuovendo un nodo dal grafo e aggiungendolo al vertex cover che si sta costruendo
            sottoProblema = ProblemaVC.Problema.espandiProblema(Problema, i)

            # Soluzione Completa ---> si controlla se "best" puo' essere aggiornato, forse l'if si puo' evitare dato che si scartano i 
            # "cammini costosi" utilizzando i controlli con il lower bound
            if ProblemaVC.Problema.checkVertexCover(sottoProblema, G):
                if len(sottoProblema.getVertici()) < best[0]:
                    best = (len(sottoProblema.getVertici()), sottoProblema.getVertici())

            # Il lower bound al problema corrente e' dato dal calcolo di un matching massimale del grafo, infatti, fissato un grafo,
            # la cardinalita' di un qualsiasi vertex cover deve essere almeno pari alla cardinalita' di un qualsiasi matching massimale.
            # Se il controllo seguente fallisce significa che sto proseguendo lungo un cammino piu' costoso del best corrente, quindi
            # non aggiungo il sottoproblema a S
            if ProblemaVC.Problema.lowerBound(sottoProblema) < best[0]:
                S.put(sottoProblema)

        del Problema
    
    return best


def main():

    G = nx.Graph()  
    G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    G.add_edges_from([(1, 2), (1, 3), (3, 4), (3, 6), (2, 7), (1, 8), (2, 10), (4, 10), (9, 10), (8, 7), (5, 6), (1, 10)])

    RG = nx.gnp_random_graph(n = 12, p = 0.3)

    exVC = exhaustiveVertexCover(RG)

    print(exVC[0], exVC[1])
    writeResultsOnFile(exVC[0], exVC[1])
    
    posRG = nx.circular_layout(RG)
    nx.draw(RG, posRG, with_labels = True, font_weight = 'bold')
    plt.show()

    '''
    posG = nx.circular_layout(G)
    nx.draw(G, posG, with_labels = True, font_weight = 'bold')
    plt.show()
    '''
    

if __name__ == '__main__':
    main()
