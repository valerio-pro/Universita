from numpy.random import random


# Applicazione sulle Catene di Markov: il giocatore entra nel casino' con "h" euro in tasca e si vuole sapere la probabilita' con cui uscira' con "n" euro in tasca.
# A ogni giocata si vince 1 euro con probabilita' "p" e si perde 1 euro con probabilita' "1-p".
# Il gioco termina quando il giocatore arriva a "n" euro oppure se arriva a 0 euro.
# Con probabilita' "h/n" il giocatore riuscira' ad arrivare a "n" euro.
def gamblersRuin(n = 20, h = 5, p = 0.5):

    numeroGiocate = 0

    while h != 0 and h != n:

        if random() <= p:
            h += 1
        else:
            h -= 1
        
        numeroGiocate += 1

    if h == 0:
        return 'Lose'

    return 'Win'


def multipleGamblersRuin(t = 100000, n = 20, h = 5, p = 0.5):

    winCount = 0
    totalCount = 0

    for _ in range(t):
        
        if gamblersRuin(n, h, p) == 'Win':
            winCount += 1

        totalCount += 1

    return winCount/totalCount


def main():

    output = multipleGamblersRuin(n = 20, h = 5, p = 0.5)
    print(f'Probabilita di vittoria stimata: {output}')


if __name__ == '__main__':
    main()
