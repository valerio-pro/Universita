from math import floor

# Algoritmo polynomial time per effettuare l'esponenziazione modulare, dati tre interi "x", "y" ed "n", si calcola "(x^y) mod n"
# Si sfrutta la seguente proprieta' della moltiplicazione modulare: (x mod n) * (y mod n) = (x * y) mod n
def esponenziazioneModulare(x, y, n):
    return potenzaRicorsiva(x, y, n)

def potenzaRicorsiva(x, y, n):

    if y <= 1:
        z = 1
    else:
        z = potenzaRicorsiva(x, floor(y/2), n)
        z = (z*z) % n
    
    if (y % 2) != 0:
        z = (z*x) % n
    
    return z


def main():

    x = 7
    y = 2
    n = 54

    z = esponenziazioneModulare(x, y, n)
    print(z)

if __name__ == '__main__':
    main()
