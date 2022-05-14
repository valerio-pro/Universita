import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib


def computeMaximumMatching(G):
    # restituisce un dizionario di coppie 
    return nx.max_weight_matching(G, maxcardinality = True)


def main():
    
    # Grafo bipartito per assegnare persone a giorni in cui sono disponibili
    BG = nx.Graph()
    BG.add_nodes_from([1, 2, 3, 4, 5, 6, 7], bipartite = 0)
    BG.add_nodes_from(['Giorno 1', 'Giorno 2', 'Giorno 3', 'Giorno 4', 'Giorno 5', 'Giorno 6', 'Giorno 7'], bipartite = 1)

    # Giorni in cui le persone sono disponibili
    BG.add_edges_from([(1, 'Giorno 2'), (1, 'Giorno 1'), (1, 'Giorno 6'), (1, 'Giorno 4'), (2, 'Giorno 1'), (2, 'Giorno 3'), (2, 'Giorno 5'), (3, 'Giorno 3'), (3, 'Giorno 5'), (4, 'Giorno 1'), (4, 'Giorno 5'), (4, 'Giorno 6'), (4, 'Giorno 7'), (5, 'Giorno 1'), (5, 'Giorno 6'), (5, 'Giorno 7'), (6, 'Giorno 3'), (6, 'Giorno 5'), (6, 'Giorno 6'), (7, 'Giorno 1'), (7, 'Giorno 2'), (7, 'Giorno 3'), (7, 'Giorno 5'), (7, 'Giorno 7')])

    MaxMatching = computeMaximumMatching(BG)
    print(MaxMatching)


    X, Y = nx.bipartite.sets(BG)
    posBG = dict()
    posBG.update( (n, (1, i)) for i, n in enumerate(X) ) # put nodes from X at x=1
    posBG.update( (n, (2, i)) for i, n in enumerate(Y) ) # put nodes from Y at x=2
    nx.draw(BG, pos = posBG, with_labels = True, font_weight = 'bold')
    plt.show()

if __name__ == '__main__':
    main()
