a = [ 1, 'a', 3, 4.5, [3, 'python', 5], [2, [4, 3.14, 5, [2, 3, [4, 2.71, '', 5]], 6]], 4, 6, [7], [3, 2, []], [4] ] 

def RecursiveSumList(a = []):      # la lista a e' composta da 18 interi, 3 float e 3 stringhe
    x = 0                      
    sum = 0                    
    while x < len(a):
        if type(a[x]) == type(1):
            sum += 1
        elif type(a[x]) == type([]):
            sum += RecursiveSumList(a[x])
        x += 1
    return sum

print(RecursiveSumList(a))
            


