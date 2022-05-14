from functools import reduce

# ["This", "is", "a", "test", "string", "from", "Andrew"]
# ordinare la lista di stringhe rispetto alla seconda lettera
print( sorted("This is a test string from Andrew".split(), key = (lambda x: x[1] if len(x) > 1 else x[0])) )  



# map(f, lista) e' un metodo che permette di applicare la funzione f alla lista di input ---> la map consente di distribuire il carico
# su piu' CPU

def my_map(f, llist):
    return [f(i) for i in llist]

print( my_map(lambda x: x+1, [1,2,3,4,5]) )  # ----> output = [2,3,4,5,6]


# reduce(f, lista), applica la funzione f ai primi 2 elementi della lista, memorizza il risultato parziale e riapplica f al
# risultato parziale e al terzo elemento e cosi' via ----> from functools import reduce

def my_reduce(f, llist):
    try:    
        if len(llist) == 2:
            return f(llist[0], llist[1])
        tmp = f(llist[0], llist[1])
        tmp_list = [tmp] + llist[2:]     
        return my_reduce(f,tmp_list)
    except:
        len(llist) == 0 or len(llist) == 1

print( my_reduce(lambda x,y: x+y, [1,2,3,4,5,6]) )   # ----> output = 21


# Calcola la somma di tutti gli interi in una lista con funzioni lambda

listaInteri = [1,2,3,4,3,2,5,1,1,1,2]

def calcolaSommaInteri(lista = []):
    return reduce(lambda x,y: x+y, lista)

# ordina una lista di coppie in ordine crescente di somma dei valori

listaCoppie = [(5,6),(1,2),(0,0),(5,4),(5,5),(1,3),(1,0)]

def ordinaCoppie(listaC = []):
    return sorted(listaC, key = ( lambda x: x[0]+x[1], listaC ))

