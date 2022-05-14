import networkx as nx  
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
        sottoProblema.Grafo.remove_node(vertice)
        sottoProblema.vertici.add(vertice)

        return sottoProblema

    
    def checkVertexCover(Problema, G):

        archi = list(G.edges)
        verticiDelProblema = Problema.getVertici()

        for (u, v) in archi:
            count = 0
            for i in verticiDelProblema:
                if i not in (u, v):
                    count += 1
            # Nessun vertice in "vertici" copre l'arco (u, v) --> "vertici" non e' un vertex cover per G
            if count == len(verticiDelProblema):
                return False

        return True

    
    def lowerBound(Problema):
        return len(nx.maximal_matching(Problema.getGrafo())) + len(Problema.getVertici())