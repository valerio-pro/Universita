import networkx as nx  
import matplotlib.pyplot as plt
import ProblemaIndependentSet as ProblemaIS


# La prima riga del file conterra' il numero di elementi dell'independent set
# Le successive len(IndependentSet) righe conterranno tutti i vertici dell'independent set trovato
# Attenzione alla directory in cui viene salvato il file
def writeResultsOnFile(number, IndependentSet):
    with open('risultatiExhaustiveIndependentSet.txt', 'w') as outFile:
        outFile.write(str(number) + '\n')
        if number > 0:
            for i in IndependentSet:
                outFile.write(str(i) + '\n')



# Algoritmo di Ricerca Esaustiva Intelligente (tecnica Branch-And-Bound) per MaxIndependentSet
def exhaustiveIndependentSet(G):

    # Se il grafo e' completamente sconnesso allora si possono prendere tutti i vertici
    if len(G.edges) == 0:
        return (len(G.nodes), set(G.nodes))
    
    Gtmp = G.copy()
    best = (0, None)
    ProblemaIniziale = ProblemaIS.Problema(Grafo = Gtmp, vertici = set())
    
    S = [ProblemaIniziale]
    while S:

        # La coda dei sottoproblemi segue una politica FIFO
        Problema = S.pop(0)
        nodiProblemaCorrente = list(Problema.getGrafo().nodes)
        
        # Il sottoproblema e' ottenuto dal problema corrente, rimuovendo un nodo "i" dal grafo e tutti i suoi vicini 
        # e aggiungendo "i" all'independent set che si sta costruendo
        for i in nodiProblemaCorrente:

            sottoProblema = ProblemaIS.Problema.espandiProblema(Problema, i)

            # Soluzione completa --> si aggiorna "best" se la soluzione trovata e' migliore
            if ProblemaIS.Problema.checkIndependentSet(sottoProblema, G):
                if len(sottoProblema.getVertici()) > best[0]:
                    best = (len(sottoProblema.getVertici()), set(sottoProblema.getVertici()))

            # Lower Bound alla dimensione dell'independent set sul sottoproblema corrente --> "n/(d+1)", dove "n" e' il numero
            # di nodi del grafo associato al sottoproblema e "d" e' il grado massimo tra i nodi dello stesso grafo + il numero di vertici
            # dell' independent set del problema corrente
            if ProblemaIS.Problema.lowerBound(sottoProblema) > best[0]:
                S.append(sottoProblema)

        del Problema
    
    return best


def main():

    G = nx.Graph()  
    G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    G.add_edges_from([(1, 2), (1, 3), (3, 4), (3, 6), (2, 7), (1, 8), (2, 10), (4, 10), (9, 10), (8, 7), (5, 6), (1, 10)])

    RG = nx.gnp_random_graph(n = 14, p = 0.3)

    exIS = exhaustiveIndependentSet(RG)

    print(exIS[0], exIS[1])
    writeResultsOnFile(exIS[0], exIS[1])
    
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