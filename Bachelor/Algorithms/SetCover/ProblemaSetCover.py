from copy import deepcopy

class Problema:

    # "F" e' la famiglia di sottoinsiemi dell'insieme universo, 
    # "S" e' il set cover che si sta costruendo associato al problema corrente
    # Sia "F" che "S" sono delle liste di insiemi
    def __init__(self, F, S):
        self.F = F
        self.S = S


    def getF(self):
        return self.F

    def getS(self):
        return self.S

    def copy(self):

        # deepcopy e' molto lenta
        # return deepcopy(self)

        copiaF = self.getF()[:]
        copiaS = self.getS()[:]

        copia = Problema(F = copiaF, S = copiaS)
        return copia


    # Si controlla se "S" e' un set cover per l'insieme universo
    def checkSetCover(S, Universe):

        unionOfSets = set()
        for i in S:
            unionOfSets = unionOfSets.union(i)

        return ( len(unionOfSets.intersection(Universe)) == len(Universe) )


    def espandiProblema(ProblemaGenitore, SubSet):
        
        sottoProblema = ProblemaGenitore.copy()

        FGenitore = ProblemaGenitore.getF()
        for i in range(0, len(FGenitore)):
            if FGenitore[i] == SubSet:
                del sottoProblema.F[i]
                break

        sottoProblema.S.append(SubSet)

        return sottoProblema 


    def lowerBound(Problema, Universe):
        pass