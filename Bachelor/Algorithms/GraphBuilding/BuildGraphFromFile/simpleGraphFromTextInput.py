import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib

'''
La prima riga del file contiene due interi "n" e "m" separati da uno spazio, 
il primo intero "n" e' il numero di nodi, il secondo intero "m" e' il numero di archi,
le successive "m" righe sono coppie di interi "u" e "v" separati da uno spazio, con "u" < "v", ad indicare l'esistenza dell'arco (u, v) nel grafo
'''

def getLinesFromFile(file = ''):
    with open(file, 'r') as strutturaGrafo:
        return [riga.strip() for riga in strutturaGrafo]


def buildGraphFromFile(file = ''):

    righe = getLinesFromFile(file)
    G = nx.Graph()
    
    infoOnNodesAndEdges = righe[0].split(' ')
    numberOfNodes = int(infoOnNodesAndEdges[0])
    
    for i in range(0, numberOfNodes):
        G.add_node(i)

    for i in righe[1:]:
        edge = i.split(' ')
        n1 = int(edge[0])
        n2 = int(edge[1])
        G.add_edge(n1, n2)

    return G


def main():

    # Assicurarsi di essere posizionati nel file system nella directory che contiene il file di testo
    G = buildGraphFromFile('simpleGraphStructure.txt')

    # Il parametro "posG" indica come verranno disposti i nodi per la visualizzazione (layout)
    posG = nx.circular_layout(G)
    nx.draw(G, posG, with_labels = True, font_weight = 'bold')
    plt.show()

if __name__ == '__main__':
    main()