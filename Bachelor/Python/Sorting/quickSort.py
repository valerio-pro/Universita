import numpy as np


def quickSort(a = [], low = 0, high = len(a)-1):
    if low < high:
        p = partition(a, low, high)
        quickSort(a, low, p-1)
        quickSort(a, p+1, high)


def partition(a, low, high):     # RANDOMIZED

    rand_pos = np.random.randint(low, high+1)
    swap(a, low, rand_pos)
    piv = a[low]
    i = low
    j = high

    while i < j:
        while a[i] <= piv and i < j:
            i += 1
        while a[j] > piv :
            j -= 1
        if i < j:
            swap(a, i, j)

    swap(a, low, j)
    return j


'''
def partition(a, low, high):    # NOT RANDOMIZED

    piv = a[low]
    i = low   # non usare i = low+1
    j = high

    while i < j:
        while a[i] <= piv and i < j:
            i += 1
        while a[j] > piv :
            j -= 1
        if i < j:
            swap(a, i, j)

    swap(a, low, j)
    return j
'''


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def main():
    
    a = []
    
    for k in range(100):
        a.append(np.random.randint(0, 100))
        
    print(a, '\n')
    quickSort(a)
    print(a)
    
if __name__ == '__main__':
    main()
