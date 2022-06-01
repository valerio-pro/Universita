from numpy.random import random


# Funzione della pedina
def pedina(n):

    # Lista dei nodi visitati dalla pedina, inizialmente si trova sul nodo 0
    visited = [0]

    # La variabile posPedina tiene conto della posizione corrente della pedina
    posPedina = 0

    # print('Pedina in 0')

    # Finche' non abbiamo visitato tutti i nodi spostiamo la pedina
    while len(visited) != n+1:

        # Si sceglie un numero u.a.r. in [0,1]
        p = random()

        # Movimento orario
        if p <= 0.5:

            posPedina = (posPedina + 1) % (n+1)

        # Movimento antiorario
        else:

            posPedina = (posPedina - 1) % (n+1)

        # print(f'Pedina in {posPedina}')

        # Se la pedina e' in un nodo nuovo allora lo si aggiunge alla lista dei nodi visitati
        if posPedina not in visited:
            visited.append(posPedina)

    return posPedina


# Funzione main
def main():

    nodo = pedina(n = 5)
    print(f"La pedina si e' fermata sul nodo {nodo}")


if __name__ == '__main__':
    main()