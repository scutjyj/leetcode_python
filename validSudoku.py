#!/usr/bin/env python
# coding=utf-8

"""
36. Valid Sudoku

Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        #check each row
        for eachStr in board:
            #ori = list(eachStr)
            #print 'running into here.'
            if '.' in eachStr:
                i = 0
                count = 0
                while i < 9:
                    if eachStr[i] != '.':
                        count += 1
                    i += 1
                oriLen = count + 1
            else:
                oriLen = len(eachStr)
            tmp = list(set(eachStr))
            if len(tmp) != oriLen:
                return False
            
        #check each column
        i = 0
        while i < 9:
            #print 'running into here.'
            eachStr = []
            j = 0
            while j < 9:
                eachStr.append(board[j][i])
                j += 1
            if '.' in eachStr:
                m = 0
                count = 0
                while m < 9:
                    if eachStr[m] != '.':
                        count += 1
                    m += 1
                oriLen = count + 1
            else:
                oriLen = len(eachStr)
            tmp = list(set(eachStr))
            #print len(tmp)
            #print oriLen
            if len(tmp) != oriLen:
                return False
            i += 1
        
        #check each block
        i = 0
        while i < 3:
            print 'running into here.'
            eachStr = ""
            j = 0
            while j < 3:
                eachStr += board[i*3+j][i*3:(i+1)*3]
                j += 1
            print eachStr
            if '.' in eachStr:
                m = 0
                count = 0
                while m < 9:
                    if eachStr[m] != '.':
                        count += 1
                    m += 1
                oriLen = count + 1
            else:
                oriLen = len(eachStr)
            tmp = list(set(eachStr))
            print len(tmp), oriLen
            if len(tmp) != oriLen:
                return False
            i += 1
        
        return True
		
s = Solution()
#board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
#board = ["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."]
#board = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
#board = [".........","4........","......6..","...38....",".5...6..1","8......6.",".........","..7.9....","...6....."]
board = ["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"]
print s.isValidSudoku(board)