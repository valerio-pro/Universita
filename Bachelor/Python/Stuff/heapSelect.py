def sin(i):
    return 2*i+1

def des(i):
    return 2*i+2

def Scambia(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

#------------------------------------------

def FixHeap(i, n, a):  

    s = sin(i)
    d = des(i)

    heapsize = n

    if s <= heapsize and a[s] > a[i]:
        massimo = s
    else:
        massimo = i

    if d <= heapsize and a[d] > a[massimo]:
        massimo = d

    if massimo != i:
        Scambia(a, massimo, i)
        FixHeap(massimo, heapsize, a)  




def Heapify(a, n):

    for i in range(n//2-1, -1, -1):   # da n//2-1 fino a 0, n//2 sarebbe divisione intera ---> casting implicito
        FixHeap(i, n, a)


def HeapSelect(a, k):   # estrae il k-esimo elemento piu' grande di a 

    n = len(a)-1
    Heapify(a, n)
    heapsize = n            # complessita' e' O(n + klog(n))

    for i in range(0, k):
        Scambia(a, 0, heapsize)
        heapsize -= 1
        FixHeap(0, heapsize, a)

    return a[0]


x = [15, 16, 3, 3, 4, 2, 4, 1, 2, 3, 4, 5, 6, 3, 0, 0, 0, 3, 2, 1, 0, 0, 10, 12, 11, 10, 1]

print(x)
print(HeapSelect(x, 2))
