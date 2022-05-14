import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib
import numpy as np # pip3 install numpy


def DFS(G, source):
    print(source)
    DFSricorsiva(G, source, esplorati = set())

def DFSricorsiva(G, nodo, esplorati):
    esplorati.add(nodo)
    for v in G.neighbors(nodo):
        if v not in esplorati:
            print(v)
            DFSricorsiva(G, v, esplorati)




def main():
    n, p = 10, 0.4
    G = nx.gnp_random_graph(n, p)
    DFS(G, 0)

    posG = nx.circular_layout(G)
    nx.draw(G, posG, with_labels = True, font_weight = 'bold')
    plt.show()


if __name__ == '__main__':
    main()