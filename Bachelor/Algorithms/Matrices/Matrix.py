class Matrix:

    def __init__(self, fromLists = []):
        if fromLists:
            self.colonne = len(fromLists[0])
        else:
            self.colonne = 0
        self.righe = len(fromLists)
        self.matrix = fromLists


    def __str__(self):
        if self:
            outString = ''
            for i in self.matrix:
                outString += (str(i) + '\n')
            return outString
        else:
            return '[]'


    def __repr__(self):
        if self:
            outString = ''
            for i in range(0, len(self.matrix)):
                if i < len(self.matrix) - 1:
                    outString += (str(self.matrix[i]) + '\n')
                else:
                    outString += (str(self.matrix[i]))
            return outString 
        else:
            return '[]'


    def getIdentityMatrix(nColonne = 0, nRighe = 0):
        if nColonne == nRighe:
            m = Matrix.get0Matrix(nColonne, nRighe)
            for i in range(0, nColonne):
                m.matrix[i][i] = 1
            return m
        else:
            return None


    def getNoneMatrix(nColonne = 0, nRighe = 0):
        return Matrix(fromLists = [[None for i in range(0, nColonne)] for j in range(0, nRighe)])

    def get0Matrix(nColonne = 0, nRighe = 0):
        return Matrix(fromLists = [[0 for i in range(0, nColonne)] for j in range(0, nRighe)])

    def get1Matrix(nColonne = 0, nRighe = 0):
        return Matrix(fromLists = [[1 for i in range(0, nColonne)] for j in range(0, nRighe)])

    def getColonne(self):
        return self.colonne

    def getRighe(self):
        return self.righe



    # Esegue il prodotto righe per colonne tra due sole matrici di input 
    # T(n) = Theta(n^3)
    def prod(M1, M2):
        if M1.getColonne() != M2.getRighe():
            return None
        M3 = Matrix.getNoneMatrix(M1.getRighe(), M2.getColonne())
        for i in range(0, M1.getRighe()):
            for j in range(0, M2.getColonne()):
                p = 0
                for k in range(0, M1.getColonne()):
                    p += (M1.matrix[i][k] * M2.matrix[k][j])
                M3.matrix[i][j] = p
        return M3

    # Esegue il prodotto righe per colonne di "n" matrici nell'ordine in cui compaiono nella lista di input
    # vengono eseguiti "n-1" prodotti tra matrici -> non ottimale
    # T(n) = Theta(n^4)
    def product(matrices):
        if len(matrices) < 2:
            return None
        Mtmp = Matrix.prod(matrices[0], matrices[1])
        for i in range(2, len(matrices)):
            M = Matrix.prod(Mtmp, matrices[i])
            Mtmp = M
        return M
