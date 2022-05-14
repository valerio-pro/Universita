

def primality_test(n):    # exponential time in the input size implementation 
    if n == 2 or n == 1:
        return True
    for i in range(2, n):
            if n%i == 0:
                print(n, ' is divisible by ', i)
                return False
    return True
            
print(primality_test(1111111111111121111111111114170111111117717))