def binarySearch(a, k, low = 0, high = len(a)-1):

    if low > high:
        return False

    if low <= high:
        
        m = int((low+high)/2)
        
        if a[m] == k:
            return True
        elif a[m] < k:
            return binarySearch(a, k, m+1, high)
        else:
            return binarySearch(a, k, low, m-1)

        

def binarySearchIterative(a, k, low = 0, high = len(a)-1):
    
    while(low <= high):
        
        m = int((low+high)/2)
        
        if a[m] == k:
            return True
        elif a[m] < k:
            low = m+1
        else:
            high = m-1
            
    return False



def main():
    
    a = [1, 2, 3, 4, 5, 6, 7, 7, 9]
    print(a)
    
    print(binarySearch(a, 6))
    print(binarySearchIterative(a, 5))
  

if __name__ == '__main__':
    main()
    
