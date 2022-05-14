from numpy.random import random


# Metodo Monte Carlo per l'approssimazione di pi-greco, per una buona approssimazione servono molte iterazioni.
def monteCarloPI(t = 100000):

    k = 0

    for _ in range(t):

        x = 2*random() - 1
        y = 2*random() - 1

        if x**2 + y**2 <= 1:
            k += 1

    return (4*k)/t


def main():

    PI = monteCarloPI()
    print(f'Approssimazione di PI: {PI}')


if __name__ == '__main__':
    main()