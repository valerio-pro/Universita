
def IntegerSort(X):

    n = len(X)
    k = max(X)
    Y = []
    
    for i in range(0, k+1):   # NB: fino a max+1
        Y.append(0)


    for i in range(0, n):
        Y[X[i]] += 1

    j = 0
    for i in range(0, k+1):   # NB: fino a max+1
        while(Y[i] > 0):
            X[j] = i
            j += 1
            Y[i] -= 1

            
            
def main():
    a = [1, 2, 3, 1, 1, 2, 5, 6, 0, 10, 3, 3, 0, 1, 21, 11, 23, 4, 7, 2, 5, 6, 7, 9, 10, 4, 0]
    print(a)
    IntegerSort(a)
    print(a)

if __name__ == '__main__':
    main()
