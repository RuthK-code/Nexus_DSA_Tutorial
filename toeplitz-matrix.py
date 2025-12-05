class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows=len(matrix)
        colu = len(matrix[0])

        for i in range(1,rows):
            for j in range(1,colu):
                if matrix[i][j] == matrix[i-1][j-1]:
                    return True
                elif matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return


s = Solution()

print(s.isToeplitzMatrix(matrix:= [[1,2],[2,2]]))
