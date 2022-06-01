from copy import deepcopy
from functools import reduce

# Classe che definisce la struttura del generico SottoProblema di Load Balancing. Ogni SottoProblema e' modellato attraverso:
# - il numero "m" di macchine, e' un'informazione statica, non cambia in realta' tra i vari sottoproblemi
# - un dizionario "assegnazioneTask" che associa ad ogni macchina la lista dei tempi di esecuzione dei task schedulati su quella macchina
# - un dizionario "taskRimanenti" che associa ad ogni task il suo tempo di esecuzione 
class Problema:

    # Inizializzazione del Problema
    def __init__(self, m, assegnazioneTask, taskRimanenti):
        self.m = m
        self.assegnazioneTask = assegnazioneTask
        self.taskRimanenti = taskRimanenti


    # Metodi "get" per recuperare informazioni specifiche sul sottoproblema
    def getTaskRimanenti(self):
        return self.taskRimanenti

    def getAssegnazioneTask(self):
        return self.assegnazioneTask

    def getCaricoPiuGrande(self):
        return ( lambda x: max([reduce(lambda x,y: x+y, value) for value in list(x.values()) if len(value) > 0]) ) (self.assegnazioneTask)
    


    # Metodo "copy" per ottenere una copia del Problema che viene poi utilizzata nel metodo "espandiProblema" per generare i vari sottoproblemi
    def copy(self):
        return deepcopy(self)



    # Metodo per verificare se il problema corrente ha costruito un'assegnazione completa dei task alle macchine, semplicemente se non
    # ci sono piu' task in "taskRimanenti" allora abbiamo una soluzione completa
    def checkSoluzioneCompleta(self):
        
        if self.taskRimanenti:
            return False
        return True



    # Il metodo seguente permette di generare "m" sottoproblemi a partire dal problema corrente e dal "task" indicato in input.
    # In particolare, per ogni i = 1, ..., m, l'i-esimo sottoproblema e' ottenuto con tre operazioni fondamentali:
    #
    #   1) Genera una copia del problema corrente che e' appunto chiamata "sottoProblema"
    #   2) Assegna il task di input alla macchina "i" (se gia' non e' stato assegnato a qualche altra macchina)
    #   3) Rimuovi il task di input dalla struttura "taskRimanenti" del "sottoProblema"
    #
    # Viene quindi ritornata la lista con questi "m" sottoproblemi 
    def espandiProblema(self, task):
        
        listaSottoProblemi = []

        for i in range(1, self.m+1):

            sottoProblema = self.copy()

            if task in sottoProblema.taskRimanenti:

                sottoProblema.assegnazioneTask[i].append(sottoProblema.taskRimanenti[task])
                sottoProblema.taskRimanenti.pop(task, None)
                listaSottoProblemi.append(sottoProblema)

        return listaSottoProblemi


    # Il lower bound al generico sottoproblema e' dato dal carico piu' grande assegnato alle macchine. Se tale carico sara' poi piu'
    # grande del best corrente, allora si potra' scartare il sottoproblema
    def lowerBound(self):
        return ( lambda x: max([reduce(lambda y,z: y+z, value) for value in list(x.values()) if len(value) > 0]) ) (self.assegnazioneTask)