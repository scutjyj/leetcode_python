#!/usr/bin/env python
# coding: utf-8

"""
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

test_case_set = [
    [[1,2,3],[4,5,6]],
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3]],
    [[1]],
    [[1,2],[3,4],[5,6]],
    [[1,2],[3,4]],
    [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
    [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
]


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rst = []
        m_num = len(matrix)
        if m_num == 0:
            return rst
        n_num = len(matrix[0])
        if n_num == 0:
            return rst
        m = n = 0
        r_num = 0
        max_round_num = min((m_num+1)/2, (n_num+1)/2)
        row_cnt = col_cnt = 0
        #print m_num, n_num, max_round_num
        while r_num < max_round_num:
            try:
                # right forward.
                while n < n_num - r_num:
                    rst.append(matrix[m][n])
                    n += 1
                row_cnt += 1
                if row_cnt == m_num:
                    return rst
                n -= 1
                m += 1
                #print 'after right:', m, n
                # down forward.
                while m <= m_num  - 1 - r_num:
                    rst.append(matrix[m][n])
                    m += 1
                col_cnt += 1
                if col_cnt == n_num:
                    return rst
                m -= 1
                n -= 1
                #print 'after down:', m, n
                # left forward.
                while n >= r_num:
                    rst.append(matrix[m][n])
                    n -= 1
                row_cnt += 1
                if row_cnt == m_num:
                    return rst
                n += 1
                m -= 1
                #print 'after left:', m, n
                while m > r_num:
                    rst.append(matrix[m][n])
                    m -= 1
                col_cnt += 1
                if col_cnt == n_num:
                    return rst
                m += 1
                n += 1
            except Exception as e:
                #print e
                return rst
            r_num += 1
        return rst

        
def test():
    s = Solution()
    for matrix in test_case_set:
        print 'input:'
        for l in matrix:
            print l
        rst = s.spiralOrder(matrix)
        print 'output:'
        print rst, '\n'
        
        
if __name__ == '__main__':
    test()