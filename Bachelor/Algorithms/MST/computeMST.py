import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib
from numpy.random import random_sample # pip3 install numpy


def computeMST(G):
    if nx.is_connected(G):
        # viene utilizzato l'algoritmo di Kruskal dal metodo seguente
        return nx.minimum_spanning_tree(G)
    return None


def main():

    G = nx.gnp_random_graph(20, random_sample())
    mst = computeMST(G)

    posG = nx.circular_layout(G)
    nx.draw(G, posG, with_labels = True, font_weight = 'bold')
    plt.show()

    if mst != None:
        posMST = nx.spring_layout(mst)
        nx.draw(mst, posMST, with_labels = True, font_weight = 'bold')
        plt.show()


if __name__ == '__main__':
    main()