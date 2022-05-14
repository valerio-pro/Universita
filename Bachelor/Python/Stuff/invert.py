a = [1, 2, 4, 6, 7, 9, 12, 13, 14, 12, 11, 8, 4, 2, 1]  # in particolare e' unimodale

def Invert(a, low = 0, high = len(a)-1):

    i = low
    j = high

    while i < j:
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
        i += 1
        j -= 1

Invert(a, 6, 12)
print(a)
