import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib
import numpy as np # pip3 install numpy


def BFS(G, source):
    frontiera = [source]
    esplorati = set()

    while frontiera:
        u = frontiera.pop(0)
        esplorati.add(u)
        print(u)
        for v in G.neighbors(u):
            if (v not in frontiera) and (v not in esplorati):
                frontiera.append(v)
                

def main():
    n, p = 6, 0.4
    G = nx.gnp_random_graph(n, p)
    BFS(G, 0)

    posG = nx.circular_layout(G)
    nx.draw(G, posG, with_labels = True, font_weight = 'bold')
    plt.show()


if __name__ == '__main__':
    main()