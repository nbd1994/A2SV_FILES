class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
    
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        self.newMat=[[0]*(col_len+1)for _ in range(row_len+1)]

        for row in range(row_len):
            prefixSum = 0
            for col in range(col_len):
                prefixSum+=matrix[row][col]
                matAbove = self.newMat[row][col+1]
                self.newMat[row+1][col+1] = prefixSum + matAbove
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 , col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        bottomRight = self.newMat[row2][col2]
        above = self.newMat[row1-1][col2]
        left = self.newMat[row2][col1-1]
        topLeft = self.newMat[row1-1][col1-1]
        return bottomRight - above -left + topLeft     
       
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)