import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib


# La prima riga del file conterra' il numero di elementi del vertex cover
# Le successive len(VertexCover) righe conterranno tutti i vertici del vertex cover trovato
# Attenzione alla directory in cui viene salvato il file
def writeResultsOnFile(number, VertexCover):
    with open('risultatiGreedyVertexCover.txt', 'w') as outFile:
        outFile.write(str(number) + '\n')
        if number > 0:
            for i in VertexCover:
                outFile.write(str(i) + '\n')


# Rimuove dal grafo "G" il nodo "v" e quindi tutti gli archi che incidono su di esso
def removeEdges(v, G):
    G.remove_node(v)
    return G


def findMaximumDegreeVertex(G):

    # "G.degree" restituisce una lista di coppie [(nodo1, gradoNodo1), (nodo2, gradoNodo2), ecc...]
    listaGradi = G.degree
    max = -1
    vertex = -1

    for i,j in listaGradi:
        if j > max:
            max = j
            vertex = i

    return vertex


def greedyVertexCover(G):

    # Grafo completamente sconnesso --> non c'e' bisogno di coprire gli archi
    if len(G.edges) == 0: 
        return (0, None)

    # Crea una copia del grafo G
    Gprimo = G.copy()

    VC = set()
    while len(Gprimo.edges) > 0:
        v = findMaximumDegreeVertex(Gprimo)
        VC.add(v)
        Gprimo = removeEdges(v, Gprimo)

    return (len(VC), VC)



def main():

    # Creazione di un grafo aleatorio
    G = nx.gnp_random_graph(n = 10, p = 0.3, seed = None, directed = False)
    
    # Esecuzione dell'algoritmo greedyVertexCover
    (number, VertexCover) = greedyVertexCover(G)

    # Scrittura su file dei risultati
    writeResultsOnFile(number, VertexCover)

    # Visualizzazione del grafo (layout circolare per la disposizione dei nodi nell'immagine)
    posG = nx.circular_layout(G)
    nx.draw(G, posG, with_labels = True, font_weight = 'bold')
    plt.show()


if __name__ == '__main__':
    main()