#Problem 2: Set matrix zeros
#U --> # You must do it in place # Will we have another than 0s and 1s?
#  --> # how many 0 will we have? 

#M --> 2D Array
#P [rows][columns]==0
#I
#R
#E

# EXAMPLE = [[1,2,3],
#            [4,5,6],
#            [7,8,9]]


# R: {0: 1, 1: }
class Solution:
    def setMatrixZeroes(self, matrix):
        ROWS = len(matrix)
        COLUMNS =len(matrix[0])
        R = {}
        C = {}

        for r in range(ROWS):
            R[r] = 1

        for c in range(COLUMNS):
            C[c] = 1

        for r in range(ROWS):
            for c in range(COLUMNS):
                if matrix[r][c] == 0:
                    R[r] = 0
                    C[c] = 0

        for r in range(ROWS):
            for c in range(COLUMNS):
                if R[r] == 0 or C[c] == 0:
                    matrix[r][c] = 0

        print(matrix)
            


s = [[1,1,1],[1,0,1],[1,1,1],[0, 1, 1]]
solution = Solution()
print(solution.setMatrixZeroes(s))
