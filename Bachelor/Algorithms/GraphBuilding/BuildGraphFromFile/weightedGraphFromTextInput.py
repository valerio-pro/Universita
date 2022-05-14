import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib


'''
La prima riga del file contiene due interi "n" e "m" separati da uno spazio, 
il primo intero "n" e' il numero di nodi, il secondo intero "m" e' il numero di archi,
le successive "m" righe sono triple di interi "u", "v" e "w" separati da uno spazio, con "u" < "v", ad indicare l'esistenza dell'arco "(u, v)" 
che ha peso "w"
'''

def getLinesFromFile(file = ''):
    with open(file, 'r') as strutturaGrafo:
        return [riga.strip() for riga in strutturaGrafo]


def buildWeightedGraphFromFile(file = ''):

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
        w = int(edge[2])
        G.add_edge(n1, n2, weight = w)

    return G

def main():

    WG = buildWeightedGraphFromFile('weightedGraphStructure.txt')

    posWG = nx.circular_layout(WG)
    edge_weight = nx.get_edge_attributes(WG, "weight")

    nx.draw(WG, posWG, with_labels = True, font_weight = 'bold')
    nx.draw_networkx_edge_labels(WG, posWG, edge_labels = edge_weight)
    plt.show()


if __name__ == '__main__':
    main()