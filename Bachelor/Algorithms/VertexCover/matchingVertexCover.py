import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib


# La prima riga del file conterra' il numero di elementi del vertex cover
# Le successive len(VertexCover) righe conterranno tutti i vertici del vertex cover trovato
# Attenzione alla directory in cui viene salvato il file
def writeResultsOnFile(number, VertexCover):
    with open('risultatiMatchingVertexCover.txt', 'w') as outFile:
        outFile.write(str(number) + '\n')
        if number > 0:
            for i in VertexCover:
                outFile.write(str(i) + '\n')


# Rimuove dal grafo "G" i nodi "u" e "v" e quindi tutti gli archi che incidono su di essi
def removeEdges(u, v, G):
    G.remove_node(u)
    G.remove_node(v)
    return G


# Seleziona un arco del grafo (il primo memorizzato)
def getEdge(G):
    return list(G.edges)[0]


# Algoritmo 2-approssimante per MinVertexCover
def matchingVertexCover(G):

    # Grafo completamente sconnesso --> non c'e' bisogno di coprire gli archi
    if len(G.edges) == 0:
        return (0, None)

    # Crea una copia del grafo G
    Gprimo = G.copy()

    VC = set()
    while len(Gprimo.edges) > 0:
        edge = getEdge(Gprimo)
        u, v = edge[0], edge[1]
        VC.add(u)
        VC.add(v)
        Gprimo = removeEdges(u, v, Gprimo)
    
    return (len(VC), VC)


def main():

    # Creazione di un grafo aleatorio
    G = nx.gnp_random_graph(n = 20, p = 0.3, seed = None, directed = False)

    # Esecuzione dell'algoritmo matchingVertexCover
    (number, VertexCover) = matchingVertexCover(G)

    # Scrittura su file dei risultati
    writeResultsOnFile(number, VertexCover)

    # Visualizzazione del grafo (layout circolare per la disposizione dei nodi nell'immagine)
    posG = nx.circular_layout(G)
    nx.draw(G, posG, with_labels = True, font_weight = 'bold')
    plt.show()


if __name__ == '__main__':
    main()