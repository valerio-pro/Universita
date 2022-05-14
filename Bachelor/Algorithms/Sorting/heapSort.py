def sin(i):
    return 2*i+1

def des(i):
    return 2*i+2

def Scambia(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

#-----------------------------------------------

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

        
# Costruzione Heap
def Heapify(a, n):

    for i in range(n//2-1, -1, -1):   # da n//2-1 fino a 0, n//2 sarebbe divisione intera ---> casting implicito
        FixHeap(i, n, a)



def HeapSort(a): 

    n = len(a)-1

    Heapify(a, n)
    heapsize = n
    
    for i in range(n, 0, -1):
        Scambia(a, i, 0)
        heapsize -= 1  # taglio la foglia, alternativamente potevo scrivere heapsize = i
        FixHeap(0, heapsize, a)
        


def main():
    a = [15, 16, 3, 3, 4, 2, 4, 1, 3.14, 2, 3, 4, 2, 5, 6, 3, 0, 0, 0, 3, 99, 23, 2, 1, 0, 0, 10, 12, 11, 10, 1]
    print(a)
    HeapSort(a)
    print(a)

if __name__ == '__main__':
    main()
