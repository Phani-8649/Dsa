class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        mat = list(map(list, zip(*matrix)))
        reversed_matrix = [row[::-1] for row in mat]
        matrix[:]=reversed_matrix