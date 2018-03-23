#!/usr/bin/env python
# coding=utf-8

"""
69. Sqrt(x)

mplement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842...,
and since we want to return an integer, the decimal part will be truncated.
"""

class Solution(object):
	def mySqrt(self, n):
		astr = str(n)
		length = len(astr)
		left = 10 ** ((length-1)/2)
		right =  10 ** ((length-1)/2+1)
		while left <= right:
			middle = (left + right)/2
			tmp  = middle ** 2
			if tmp == n:
				return middle
			elif tmp > n:
				right = middle - 1
			else:
				left  = middle + 1
		#print left, right, middle
		return right
		
s = Solution()
print s.mySqrt(123456789012345678901234567890)
	
		