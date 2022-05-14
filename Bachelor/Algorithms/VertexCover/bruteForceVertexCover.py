import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib
import numpy as np # pip3 install numpy
from itertools import combinations

# La prima riga del file conterra' il numero di elementi del vertex cover
# Le successive len(VertexCover) righe conterranno tutti i vertici del vertex cover trovato
# Attenzione alla directory in cui viene salvato il file
def writeResultsOnFile(number, VertexCover):
    with open('risultatiBruteForceVertexCover.txt', 'w') as outFile:
        outFile.write(str(number) + '\n')
        if number > 0:
            for i in VertexCover:
                outFile.write(str(i) + '\n')


# Controlla se "vertici" e' un vertex cover per G
def checkVertexCover(G, vertici = set()):
    for (u, v) in G.edges:
        count = 0
        for i in vertici:
            if i not in (u, v):
                count += 1
        # Nessun vertice in "vertici" copre l'arco (u, v) --> "vertici" non e' un vertex cover per G
        if count == len(vertici):
            return False
    return True


# Restituisce tutte i possibili sottoinsiemi di "k" elementi dell'insieme "vertici" di input
# "combinations(vertici, k)" restituisce un iteratore di tuple di "k" elementi
def kSubsets(vertici, k):
    return combinations(vertici, k)



# Algoritmo brute force che restituisce il vertex cover di cardinalita' minima per il grafo "G" di input
def bruteForceVertexCover(G):

    # Grafo completamente sconnesso --> non c'e' bisogno di coprire gli archi
    if len(G.edges) == 0:
        return (0, None)

    # Partendo da k = 0, esamina tutti i possibili sottoinsiemi di k nodi e verifica se effettivamente sono un vertex cover
    # per il grafo di input. Il primo sottoinsieme di k nodi trovato deve essere necessariamente il vertex cover di
    # cardinalita' minima
    for k in range(0, len(G.nodes)):
        candidatiVC = kSubsets(set(G.nodes), k)
        for candidato in candidatiVC:
            if checkVertexCover(G, set(candidato)):
                return (len(candidato), set(candidato))
    
    # return di "sicurezza"
    return (len(G.nodes), set(G.nodes))



# Questa funzione (brute force) restituisce una lista di tutti i possibili vertex cover del grafo "G" di input
def getAllVertexCover(G):

    # Grafo completamente sconnesso --> non c'e' bisogno di coprire gli archi
    if len(G.edges) == 0:
        return [None]

    # Partendo da k = 0, esamina tutti i possibili sottoinsiemi di k nodi e verifica se effettivamente sono un vertex cover
    # per il grafo di input. Il primo sottoinsieme di k nodi trovato deve essere necessariamente il vertex cover di
    # cardinalita' minima
    res = []
    for k in range(0, len(G.nodes)):
        candidatiVC = kSubsets(set(G.nodes), k)
        for candidato in candidatiVC:
            if checkVertexCover(G, set(candidato)):
                res.append(set(candidato))
        # Una volta che abbiamo trovato un vertex cover di cardinalita' k allora tutti gli altri vertex cover di 
        # cardinalita' minima hanno sempre cardinalita' k
        if len(res) > 0:
            return res

    # return di "sicurezza"
    return [set(G.nodes)]


def main():

    # Creazione di un grafo aleatorio
    G = nx.gnp_random_graph(n = 6, p = 0.3, seed = None, directed = False)
    
    # Esecuzione dell'algoritmo brute force per trovare il vertex cover di cardinalita' minima
    (number, VC) = bruteForceVertexCover(G)

    print("Cardinalita' del minimo Vertex Cover: " + str(number) + ",",  "Vertex Cover:", VC)

    # Scrittura dei risultati su file
    writeResultsOnFile(number, VC)

    # Visualizzazione del grafo (layout circolare per la disposizione dei nodi nell'immagine)
    posG = nx.circular_layout(G)
    nx.draw(G, posG, with_labels = True, font_weight = 'bold')
    plt.show()
    

if __name__ == '__main__':
    main()
