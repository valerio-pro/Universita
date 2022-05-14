import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib
from numpy.random import randint # pip3 install numpy
from itertools import combinations


# La prima riga del file conterra' il numero di elementi dell'independent set
# Le successive len(IndependentSet) righe conterranno tutti i vertici dell'independent set trovato
# Attenzione alla directory in cui viene salvato il file
def writeResultsOnFile(number, IndependentSet):
    with open('risultatiBruteForceIndependentSet.txt', 'w') as outFile:
        outFile.write(str(number) + '\n')
        if number > 0:
            for i in IndependentSet:
                outFile.write(str(i) + '\n')



# Dato il grafo "G" e l'insieme "vertici", si verifica se "vertici" e' un independent set di "G"
def checkIndependentSet(G, vertici = set()):
    for i in vertici:
        for j in vertici:
            # Se "i" e "j" non sono lo stesso vertice allora controlliamo se "j" e' adiacente a "i" nel grafo
            # Se "j" e' adiacente a "i" allora "vertici" non e' un independent set
            if i != j:
                if j in G.neighbors(i):
                    return False
    return True



# Restituisce tutte i possibili sottoinsiemi di "k" elementi dell'insieme "vertici" di input
# "combinations(vertici, k)" restituisce un iteratore di tuple di "k" elementi
def kSubsets(vertici, k):
    return combinations(vertici, k)



# Algoritmo brute force per trovare l'independent set di cardinalita' massima del grafo "G" di input
def bruteForceIndependentSet(G):

    # Grafo completamente sconnesso --> si possono prendere tutti i vertici del grafo
    if len(G.edges) == 0:
        return (len(G.nodes), set(G.nodes))


    # Partendo da k = len(G.nodes) e fino a k = 1, esamina tutti i possibili sottoinsiemi di k nodi e verifica se effettivamente sono un 
    # independent set per il grafo di input. Il primo sottoinsieme di k nodi trovato deve essere necessariamente l'independent set di
    # cardinalita' massima
    for k in range(len(G.nodes), 0, -1):
        candidatiIS = kSubsets(set(G.nodes), k)
        for candidato in candidatiIS:
            if checkIndependentSet(G, set(candidato)):
                return (len(candidato), set(candidato))
    
    # return di "sicurezza"
    if len(G.nodes) >= 1:
        # Ritorna un vertice qualunque
        return (1, set(list(G.nodes)[randint(0, len(G.nodes))]))
    return (0, None)



# Questa funzione (brute force) restituisce una lista di tutti i possibili independent set del grafo "G" di input
def getAllIndependentSet(G):

    # Grafo completamente sconnesso --> si possono prendere tutti i vertici del grafo
    if len(G.edges) == 0:
        return [set(G.nodes)]


    # Partendo da k = len(G.nodes) e fino a k = 1, esamina tutti i possibili sottoinsiemi di k nodi e verifica se effettivamente sono un 
    # independent set per il grafo di input. Il primo sottoinsieme di k nodi trovato deve essere necessariamente l'independent set di
    # cardinalita' massima
    res = []
    for k in range(len(G.nodes), 0, -1):
        candidatiIS = kSubsets(set(G.nodes), k)
        for candidato in candidatiIS:
            if checkIndependentSet(G, set(candidato)):
                res.append(set(candidato))
        if len(res) > 0:
            return res
        
    # return di "sicurezza"
    if len(G.nodes) >= 1:
        # Ritorna un vertice qualunque
        return [set(list(G.nodes)[randint(0, len(G.nodes))])]
    return [None]



def main():

    # Creazione di un grafo aleatorio
    G = nx.gnp_random_graph(n = 10, p = 0.3, seed = None, directed = False)
    
    # Esecuzione dell'algoritmo brute force per trovare l'independent set di cardinalita' massima
    (number, IS) = bruteForceIndependentSet(G)

    print("Cardinalita' del massimo Independent Set: " + str(number) + ",",  "Independent Set:", IS)
    
    # Scrittura dei risultati su file
    writeResultsOnFile(number, IS)

    # Visualizzazione del grafo (layout circolare per la disposizione dei nodi nell'immagine)
    posG = nx.circular_layout(G)
    nx.draw(G, posG, with_labels = True, font_weight = 'bold')
    plt.show()
    

if __name__ == '__main__':
    main()