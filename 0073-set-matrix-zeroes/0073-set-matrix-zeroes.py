class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        a=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]==0):
                    a.append([i,j]) 
                    # to store the index where the '0' elemets sare present
        for a,b in a:
            for i in range(len(matrix)):
                matrix[i][b]=0
            for j in range(len(matrix[0])):
                matrix[a][j]=0