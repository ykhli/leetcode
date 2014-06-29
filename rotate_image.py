#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix = [[0]]
import numpy as np

class Solution:
    def rotate(self,matrix):
        dim = len(matrix)
        if(dim == 1):
            return matrix

        newmat = [[0 for x in xrange(dim)] for x in xrange(dim)]

        for row in range(0,len(matrix)):
            for col in range(0,len(matrix)):
                print row,col
                newmat[row][col] = matrix[dim-1-col][row]
        return newmat

if __name__ =="__main__":
    x = Solution()
    print x.rotate(matrix)
