#!/usr/bin/env python
# coding=utf-8

"""
9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.
"""

def isPalindromic(string):
	if len(string) == 1:
		return True
	elif len(string) == 2:
		if string[0] == string[1]:
			return True
		else:
			return False
	else:
		if string[0] == string[-1]:
			return isPalindromic(string[1:-1])
		else:
			return False
			
if __name__ == '__main__':
	string = raw_input('Enter a string:')
	print isPalindromic(string)