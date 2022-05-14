a = [1, 2, 3, 4, 5, 6, 7, 7, 9]

def RicercaBinariaRic(a, k, low = 0, high = len(a)-1):

    if low > high:
        return False

    if low <= high:
        m = int((low+high)/2)
        if a[m] == k:
            return True
        elif a[m] < k:
            return RicercaBinariaRic(a, k, m+1, high)
        else:
            return RicercaBinariaRic(a, k, low, m-1)


def RicercaBinariaIt(a, k, low = 0, high = len(a)-1):
    while(low <= high):
        m = int((low+high)/2)
        if a[m] == k:
            return True
        elif a[m] < k:
            low = m+1
        else:
            high = m-1
    return False

print(RicercaBinariaRic(a, 6))

print(RicercaBinariaIt(a, 5))
