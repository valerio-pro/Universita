from numpy.random import randint


def randomQuickSort(A = []):
    
    if len(A) <= 1:
        return A

    pivotPosition = randint(low = 0, high = len(A))
    pivot = A[pivotPosition]
    del A[pivotPosition]

    left, right = [], []

    for element in A:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)
    
    return randomQuickSort(left) + [pivot] + randomQuickSort(right)


def main():

    A = list(randint(low = -100, high = 100, size = 100))
    print(A)
    A = randomQuickSort(A)
    print(A)


if __name__ == '__main__':
    main()
