import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib


def main():
    # Generare un grafo non orientato e pesato

    G = nx.Graph()  # fare G = nx.DiGraph() se si vuole un grafo orientato

    G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    G.add_edges_from([(1, 2, {"weight": 12}), (1, 3, {"weight": 10}), (2, 3, {"weight": 8}), (2, 4, {"weight": 8}), (3, 4, {"weight": 2}), (3, 5, {"weight": 3}), (3, 6, {"weight": 6}), (2, 7, {"weight": 8}), (1, 8, {"weight": 31}), (2, 10, {"weight": 20}), (3, 5, {"weight": 10}), (9, 10, {"weight": 23}), (8, 7, {"weight": 22}), (7, 6, {"weight": 1}),
                    (5, 6, {"weight": 19}), (6, 9, {"weight": 11}), (1, 10, {"weight": 2})])

    
    '''
    Edges = G.edges
    Nodes = G.nodes
    print(Edges)
    print(Nodes)
    '''

    # il parametro "posG" indica come verranno disposti i nodi per la visualizzazione (layout)
    posG = nx.circular_layout(G)
    edge_weight = nx.get_edge_attributes(G, "weight")
    nx.draw(G, posG, with_labels = True, font_weight = 'bold')
    nx.draw_networkx_edge_labels(G, posG, edge_labels = edge_weight)
    plt.show()

if __name__ == '__main__':
    main()