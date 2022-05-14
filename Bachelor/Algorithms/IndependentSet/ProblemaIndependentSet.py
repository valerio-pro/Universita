from math import ceil, floor, sqrt
from copy import deepcopy

class Problema:

    def __init__(self, Grafo, vertici):
        self.Grafo = Grafo
        self.vertici = vertici

    
    def copy(self):

        # deepcopy() e' molto lenta 
        # copia = deepcopy(self)
        
        Gp = self.getGrafo().copy()
        vp = set(list(self.getVertici())[:])
        copia = Problema(Grafo = Gp, vertici = vp)

        return copia

    def getVertici(self):
        return self.vertici

    def getGrafo(self):
        return self.Grafo

    
    def espandiProblema(ProblemaGen, vertice):

        sottoProblema = ProblemaGen.copy()
        vicini = list(ProblemaGen.getGrafo().neighbors(vertice))

        for i in vicini:
            sottoProblema.Grafo.remove_node(i)
            
        sottoProblema.Grafo.remove_node(vertice)
        sottoProblema.vertici.add(vertice)

        return sottoProblema

    
    # Dato il grafo "G" e un sottoproblema, si verifica se i vertici raccolti nel sottoproblema sono un independent set di "G"
    def checkIndependentSet(Problema, G):
        vertici = Problema.getVertici()
        for i in vertici:
            for j in vertici:
                # Se "i" e "j" non sono lo stesso vertice allora controlliamo se "j" e' adiacente a "i" nel grafo
                # Se "j" e' adiacente a "i" allora "vertici" non e' un independent set
                if i != j:
                    if j in G.neighbors(i):
                        return False
        return True

    
    # Il lower bound alla dimensione dell'independent set e': "n/(d+1)" 
    # dove "n" e' il numero di nodi e "d" e' il grado massimo dei vertici
    def lowerBound(Problema):

        # Si ottiene un iteratore (nodo, grado) per ogni nodo del grafo
        nodo_grado = Problema.getGrafo().degree
        maxDegree = 0

        for _,j in nodo_grado:
            if j > maxDegree:
                maxDegree = j 

        return (ceil(len(Problema.getGrafo().nodes)/(maxDegree + 1))) + len(Problema.getVertici()) 


    # L'upper bound al problema corrente e' dato da una disuguaglianza che limita la size del massimo independent set,
    # tale disuguaglianza e' riportata in un paper (link: https://www.sciencedirect.com/science/article/abs/pii/S0166218X18304062)
    def upperBound(Problema):
        return floor( 0.5 + sqrt( 0.25 + (len(Problema.getGrafo().nodes)**2) - len(Problema.getGrafo().nodes) - (2 * len(Problema.getGrafo().edges)) ) )