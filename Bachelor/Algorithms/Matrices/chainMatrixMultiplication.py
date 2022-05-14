import Matrix as mc

# Algoritmo di Programmazione Dinamica
# Restituisce il numero ottimale (cioe' minimo) di moltiplicazioni per effetturare la moltiplicazione tra una sequenza di matrici di input
# Viene sfruttata la proprieta' associativa del prodotto righe per colonne tra matrici, la proprieta' commutativa non vale
# T(n) = O(n^3)
# S(n) = O(n^2)
def chainMatrixMultiplication(matrici = []):

    n = len(matrici)
    c = 100000
    M = mc.Matrix.getNoneMatrix(nColonne = n, nRighe = n)    

    for i in range(0, n):
        M.matrix[n-i-1][i] = 0
    #print(M)

    for s in range(1, n):
        for i in range(0, n-s):
            j = i+s
            globMin = c
            for k in range(i, j):
                currMin = ( matrici[i].getRighe()*matrici[j].getColonne()*matrici[k].getColonne() ) + M.matrix[n-i-1][k] + M.matrix[n-k-2][j]
                if currMin < globMin:
                    globMin = currMin
            if globMin < c:
                M.matrix[n-i-1][j] = globMin
                #print(M)

    # M.matrix[n-1][n-1] contiene il numero ottimale di moltiplicazioni tra elementi della matrice
    #return M.matrix[n-1][n-1]
    return M

# findSolution() restituisce la matrice data dal prodotto di tutte le matrici, esegue i prodotti tra le matrici in modo da rendere
# minimo il numero di prodotti tra gli elementi delle matrici stesse 
def findSolution(matrici = []):
    global M
    M = chainMatrixMultiplication(matrici)
    return proceduraRicorsiva(0, len(matrici)-1, matrici)

def proceduraRicorsiva(i, j, matrici):
    
    if i == j:
        return matrici[i]
    
    k = i
    while M.matrix[len(matrici)-i-1][j] != ( ( matrici[i].getRighe()*matrici[j].getColonne()*matrici[k].getColonne() ) + M.matrix[len(matrici)-i-1][k] + M.matrix[len(matrici)-k-2][j] ):
        k += 1

    return mc.Matrix.prod(proceduraRicorsiva(i, k, matrici), proceduraRicorsiva(k+1, j, matrici))



def main():
    
    m1 = mc.Matrix(fromLists = [[1, 2, 2], [2, 2, 2]])
    m2 = mc.Matrix(fromLists = [[1, 2], [2, 1], [1, 1]])
    m3 = mc.Matrix(fromLists = [[1, 1], [2, 1]])
    m4 = mc.Matrix(fromLists = [[1, 2], [2, 1]])
    #print(m1, f'colonne = {m1.getColonne()}', ' ', f'righe = {m1.getRighe()}')

    '''
    result1 = chainMatrixMultiplication([m1, m2, m3, m4])
    print(result1)
    '''

    t1 = mc.Matrix(fromLists = [[1, 2, 2], [2, 2, 2]])
    t2 = mc.Matrix(fromLists = [[1, 2, 1, 1], [2, 1, 3, 2], [1, 1, 2, 3]])
    t3 = mc.Matrix(fromLists = [[1, 1, 1, 2, 2], [2, 1, 3, 4, 1], [4, 2, 3, 2, 1], [1, 1, 1, 4, 2]])

    '''
    result2 = chainMatrixMultiplication([t1, t2, t3])
    print(result2)
    '''

    res = findSolution([m1, m2, m3, m4])
    print(res)
    

if __name__ == '__main__':
    main()
