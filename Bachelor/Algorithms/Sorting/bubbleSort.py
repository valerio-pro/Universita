def Scambia(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def BubbleSort(a, low = 0, high = len(a)-1):

    i = low

    for i in range(high):
        for j in range(high-i):
            if a[j] > a[j+1]:
                Scambia(a, j, j+1)

def main():
    a = [3, 4, 2, 2, 1, 1, 1, 8, 8, 8, 9, 9, 9, 10, 0, 0, 9, 8, 7, 8]
    BubbleSort(a)
    print(a)
    
if __name__ == '__main__':
    main()
