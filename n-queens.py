#!/usr/bin/env python
# coding=utf-8

"""
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution(object):
	
	def locateQ(self, i, j, n, tmp):
		while j < n:
			k = 0
			hasQ = 0
			while k < i:
				if tmp[k][j] == 'Q':
					hasQ = 1
					break
				k += 1
			if hasQ == 1:
				j += 1
				continue
			k = j - 1
			hasQ = 0
			while k >= 0:
				if j - k > i:
					break
				else:
					if tmp[i-(j-k)][k] == 'Q':
						hasQ = 1
						break
					else:
						k -= 1
			if hasQ == 1:
				j += 1
				continue
			k = j + 1
			while k < n:
				if k - j > i:
					break
				else:
					if tmp[i-(k-j)][k] == 'Q':
						hasQ = 1
						break
					else:
						k += 1
			if hasQ == 1:
				j += 1
				continue
			break
		return j	
	
	def nqueens(self, n):
		
		"""
		type(n): int 
		return type: list[list[str]]
		"""
		
		import copy
		ret = []
		if n < 4:
			return ret
		tmp = ['Q'+'.'*(n-1)]
		i = 1
		while len(tmp) != 0:
			if i == n:
				print "adding:"
				print tmp
				ret.append(copy.deepcopy(tmp))
				tmp.pop()
				i -= 2
				print ret,tmp
				pq = tmp[i].index('Q') + 1
				print 'pq=%s' % pq
				j = self.locateQ(i, pq, n, tmp)
				while j == n:
					tmp.pop()
					i -= 1
					if i == 0:
						pq = tmp[i].index('Q') + 1
						if pq == n:
							return ret
						else:
							newStr = '.'*pq + 'Q' + '.'*(n-pq-1)
							tmp.pop()
							tmp.append(newStr)
							i += 1
							break
					else:
						pq = tmp[i].index('Q') + 1
						j = self.locateQ(i, pq, n, tmp)
				else:
					newStr = '.'*j + 'Q' + '.'*(n-j-1)
					tmp.pop()
					tmp.append(newStr)
					i += 1
				
			else:
				j = self.locateQ(i, 0, n, tmp)
				print 'j=%s,i=%s' % (j,i)
				if j < n:
					newStr = '.'*j + 'Q' + '.'*(n-j-1)
					tmp.append(newStr)
					i += 1
				else:
					i -= 1
					if i == 0:
						#TODO:
						pq = tmp[i].index('Q') + 1
						if pq == n:
							return ret
						else:
							newStr = '.'*pq + 'Q' + '.'*(n-pq-1)
							tmp.pop()
							tmp.append(newStr)
							i += 1						
							continue
					pq = tmp[i].index('Q') + 1
					j = self.locateQ(i, pq, n, tmp)
					print 'pq=%s,j=%s' % (pq,j)
					while j == n:
						tmp.pop()
						i -= 1
						if i == 0:
							pq = tmp[i].index('Q') + 1
							if pq == n:
								return ret
							else:
								newStr = '.'*pq + 'Q' + '.'*(n-pq-1)
								tmp.pop()
								tmp.append(newStr)
								i += 1
								break
						else:
							pq = tmp[i].index('Q') + 1
							j = self.locateQ(i, pq, n, tmp)
					else:
						newStr = '.'*j + 'Q' + '.'*(n-j-1)
						tmp.pop()
						tmp.append(newStr)
						i += 1
						
	"""
	Use the DFS helper function to find solutions recursively. A solution will be found when the length of queens is equal to n ( queens is a list of the indices of the queens).
	In this problem, whenever a location (x, y) is occupied, any other locations (p, q ) where p + q == x + y or p - q == x - y would be invalid. We can use this information 
	to keep track of the indicators (xy_dif and xy_sum ) of the invalid positions and then call DFS recursively with valid positions only. 
	At the end, we convert the result (a list of lists; each sublist is the indices of the queens) into the desire format.
	"""
	def solveNQueens(self, n):
		def DFS(queens, xy_dif, xy_sum):
			p = len(queens)
			if p==n:
				result.append(queens)
				return None
			for q in range(n):
				if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
					DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
		result = []
		DFS([],[],[])
		return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
				
"""		
s = Solution()
#tmp = ['Q....', '...Q.', '.Q...']
tmp = ['Q....', '....Q', '..Q..']
print s.locateQ(3, 0, 5, tmp)
"""				
s = Solution()
b = s.nqueens(5)
print b
a = [["Q....","..Q..","....Q",".Q...","...Q."],["Q....","...Q.",".Q...","....Q","..Q.."],[".Q...","...Q.","Q....","..Q..","....Q"],[".Q...","....Q","..Q..","Q....","...Q."],["..Q..","Q....","...Q.",".Q...","....Q"],["..Q..","....Q",".Q...","...Q.","Q...."],["...Q.","Q....","..Q..","....Q",".Q..."],["...Q.",".Q...","....Q","..Q..","Q...."],["....Q",".Q...","...Q.","Q....","..Q.."],["....Q","..Q..","Q....","...Q.",".Q..."]]
print a == b	