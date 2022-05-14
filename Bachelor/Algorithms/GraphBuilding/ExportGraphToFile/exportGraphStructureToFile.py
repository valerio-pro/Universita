import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib


# Esporta su file un grafo pesato
def exportWeightedGraphToFile(G):
    # dizionario --> (u, v): weight(u,v)
    edge_weight = nx.get_edge_attributes(G, "weight")  
    with open('strutturaGrafoPesato.txt', 'w') as file:
        file.write(str(len(G.nodes)) + ' ' + str(len(G.edges)) + '\n')
        for i in G.edges:
            u = i[0]
            v = i[1]
            weight = edge_weight[(u, v)]
            file.write(str(u) + ' ' + str(v) + ' ' + str(weight) + '\n')


# Esporta su file un grafo non pesato
def exportGraphToFile(G):
    with open('strutturaGrafo.txt', 'w') as file:
        file.write(str(len(G.nodes)) + ' ' + str(len(G.edges)) + '\n')
        for i in G.edges:
            u = i[0]
            v = i[1]
            file.write(str(u) + ' ' + str(v) + '\n')

def main():

    n = 10
    p = 0.2
    G = nx.gnp_random_graph(n, p)

    WG = nx.Graph()  # fare G = nx.DiGraph() se si vuole un grafo orientato

    WG.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    WG.add_edges_from([(1, 2, {"weight": 12}), (1, 3, {"weight": 10}), (2, 3, {"weight": 8}), (2, 4, {"weight": 8}), (3, 4, {"weight": 2}), (3, 5, {"weight": 3}), (3, 6, {"weight": 6}), (2, 7, {"weight": 8}), (1, 8, {"weight": 31}), (2, 10, {"weight": 20}), (3, 5, {"weight": 10}), (9, 10, {"weight": 23}), (8, 7, {"weight": 22}), (7, 6, {"weight": 1}),
                    (5, 6, {"weight": 19}), (6, 9, {"weight": 11}), (1, 10, {"weight": 2})])

    if nx.is_weighted(G):
        exportWeightedGraphToFile(G)
    else:
        exportGraphToFile(G)

    posRG = nx.circular_layout(G)
    nx.draw(G, posRG, with_labels = True, font_weight = 'bold')
    plt.show()

    if nx.is_weighted(WG):
        exportWeightedGraphToFile(WG)
    else:
        exportGraphToFile(WG)
    

if __name__ == '__main__':
    main()