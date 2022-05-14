# Vengono eseguite al piu' O(n) chiamate ricorsive
# Supponendo che la divisione abbia costo costante, T(n) = O(n)
def eu(a = 1, b = 1):
    if b == 0:
        return a
    return eu(b, a%b)

def main():
    a = 245
    b = 49
    print(a, b)
    print(eu(a, b))
   
if __name__ == '__main__':
    main()
