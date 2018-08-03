#!/usr/bin/env python
# coding: utf-8

"""
48. Rotate Image
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""

test_case_set = [
    [[1,2], [3,4]],
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
]


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        # reverse the matrix row by row firstly.
        i = 0
        n = len(matrix)
        if n <= 1:
            return
        while i < n:
            #matrix[i].reverse()
            s = 0
            e = n - 1
            while s < e:
                matrix[i][s], matrix[i][e] = matrix[i][e], matrix[i][s]
                s += 1
                e -= 1
            i += 1
        # exchange the element diagonally from the left bottom to the diagonal.
        line_num = 1
        s_r = n - line_num - 1
        s_c = 0
        while line_num < n:
            cnt = 0
            e_r = s_r + line_num
            e_c = s_c + line_num
            l = line_num + 1
            while cnt < l / 2:
                matrix[s_r+cnt][s_c+cnt], matrix[e_r-cnt][e_c-cnt] = matrix[e_r-cnt][e_c-cnt], matrix[s_r+cnt][s_c+cnt]
                cnt += 1
            s_r -= 1
            line_num += 1
        # exchange the element diagonally from the right top to the diagonal.
        line_num = 1
        s_r = 1
        s_c = n - 1
        while line_num < n - 1:
            cnt = 0
            e_r = s_r - line_num
            e_c = s_c - line_num
            l = line_num + 1
            while cnt < l / 2:
                matrix[s_r-cnt][s_c-cnt], matrix[e_r+cnt][e_c+cnt] = matrix[e_r+cnt][e_c+cnt], matrix[s_r-cnt][s_c-cnt]
                cnt += 1
            s_r += 1
            line_num += 1
            

def test():
    s = Solution()
    for matrix in test_case_set:
        print 'input:'
        for l in matrix:
            print l
        s.rotate(matrix)
        print 'output:'
        for l in matrix:
            print l
        print ''
        
        
if __name__ == '__main__':
    test()
        
                

        
        