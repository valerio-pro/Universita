import networkx as nx  # pip3 install networkx
import matplotlib.pyplot as plt # pip3 install matplotlib


'''
La prima riga contiene un intero "n" ad indicare il numero di nodi che deve avere il grafo e un float "p" ad indicare la probabilita' che 
esiste un arco tra ogni coppia di nodi del grafo
'''

def getLinesFromFile(file = ''):
    with open(file, 'r') as strutturaGrafo:
        return [riga.strip() for riga in strutturaGrafo]


def buildRandomGraphFromFile(file = ''):

    riga = getLinesFromFile(file)
    infoOnGraphStructure = riga[0].split(' ')

    n = int(infoOnGraphStructure[0])
    p = float(infoOnGraphStructure[1])

    RG = nx.gnp_random_graph(n, p)

    return RG


def main():

    # Assicurarsi di essere posizionati nel file system nella directory che contiene il file di testo
    RG = buildRandomGraphFromFile('randomGraphStructure.txt')

    # Il parametro "posRG" indica come verranno disposti i nodi per la visualizzazione (layout)
    posRG = nx.circular_layout(RG)
    nx.draw(RG, posRG, with_labels = True, font_weight = 'bold')
    plt.show()


if __name__ == '__main__':
    main()