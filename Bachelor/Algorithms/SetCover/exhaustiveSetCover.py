import ProblemaSetCover as ProblemaSC


# La prima riga del file mostrera' l'insieme "Universo"
# La seconda riga del file mostrera' la cardinalita' del minimo set cover trovato
# Le successive len(SetCover) righe mostreranno tutti i sottoinsiemi del minimo set cover trovato
# Attenzione alla directory in cui e' salvato il file 
def writeResultsOnFile(Universo, SetCover):
    with open('risultatiExhaustiveSetCover.txt', 'w') as fileOut:
        fileOut.write(str(Universo) + '\n')
        fileOut.write(str(len(SetCover)) + '\n')
        for i in SetCover:
            fileOut.write(str(i) + '\n')


# Algoritmo di Ricerca Esaustiva Intelligente (tecnica Branch-And-Bound) per MinSetCover
def exhaustiveSetCover(U, F):
    
    # Un problema e' modellato come una famiglia di insiemi "F" che rappresenta i sottoinsiemi ancora da analizzare e
    # come una sottofamiglia di insiemi "S" che rappresenta gli insiemi che stiamo prendendo nel set cover
    ProblemaIniziale = ProblemaSC.Problema(F = F, S = [])
    best = (len(F), F)

    S = [ProblemaIniziale]
    while S:
        
        # La coda dei sottoproblemi segue una politica FIFO
        Problema = S.pop(0)
        sottoinsiemiProblemaCorrente = Problema.getF()

        for i in sottoinsiemiProblemaCorrente:
            
            # Un sottoproblema e' ottenuto dal problema corrente, prendendo un insieme, rimuovendolo da "F" e aggiungendolo a "S"
            sottoProblema = ProblemaSC.Problema.espandiProblema(Problema, i)

            # Si controlla se la soluzione e' completa --> eventualmente si aggiorna "best"
            if ProblemaSC.Problema.checkSetCover(sottoProblema.getS(), U):
                if len(sottoProblema.getS()) < best[0]:
                    best = (len(sottoProblema.getS()), sottoProblema.getS())

            # Lower Bound molto semplice --> nel prossimo sottoproblema devo prendere almeno un altro insieme dalla famiglia
            if 1 + len(sottoProblema.getS()) < best[0]:
                S.append(sottoProblema)

        del Problema

    return best


def main():

    U1 = set([1, 2, 3, 4, 5, 6])
    F1 = [set([1, 6]), set([1, 2, 3]), set([2, 5]), set([2, 3, 4]), set([3, 4])]
    
    U2 = set([1, 2, 3, 4, 5, 6, 7])
    F2 = [set([1, 6]), set([1, 2, 3]), set([2, 5]), set([2, 3, 4]), set([3, 4]), set([1, 7]), set([1, 2, 7])]
    
    exSC1 = exhaustiveSetCover(U1, F1)
    exSC2 = exhaustiveSetCover(U2, F2)

    print(exSC1)
    print(exSC2)
    # writeResultsOnFile(U1, exSC1[1])
    


if __name__ == '__main__':
    main()
