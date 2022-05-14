import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib
from numpy.random import random_sample # pip3 install numpy


# Generare un grafo aleatorio "G_n,p" con "n" nodi e probabilita' "p" che ci sia un arco tra ogni coppia di nodi

def getRandomGraph(n = 10, p = random_sample()):
    RG = nx.gnp_random_graph(n, p, seed = None, directed = False)
    if nx.is_connected(RG):
        print("Il grafo e' connesso")
    else:
        print("Il grafo non e' connesso")
    return RG


def main():
    randomGraph = getRandomGraph(n = 20, p = 0.2)

    # il parametro "posRG" indica come verranno disposti i nodi per la visualizzazione (layout)
    posRG = nx.circular_layout(randomGraph)
    nx.draw(randomGraph, posRG, with_labels = True, font_weight = 'bold')
    plt.show()

if __name__ == '__main__':
    main()