from time import perf_counter


def elevazionePotenza(x, y = 0):
    return x**y


# Schema generale per misurare il tempo di esecuzione (in secondi) di una funzione 
# --> si usa il metodo "perf_counter()" della libreria "time"
def getExecutionTime(function, input):

    x, y = input
    start = perf_counter()
    res = function(x, y)
    end = perf_counter()

    return res, end - start



def main():

    result, execTime = getExecutionTime(elevazionePotenza, (12, 10))
    print(f'Output -> {result}\nTempo di Esecuzione -> {execTime}')


if __name__ == '__main__':
    main()