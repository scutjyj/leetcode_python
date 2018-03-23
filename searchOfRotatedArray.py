#!/usr/bin/env python
# coding=utf-8

"""
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        
        def binarySearch(A, left, right, target):
            while left <= right:
                center = (left + right)/2
                if target == A[center]:
                    return center
                elif target > A[center]:
                    left = center + 1
                else:
                    right = center - 1
            return -1
        
        lenOfA = len(A)
        if lenOfA == 0:
            return -1
        if lenOfA == 1:
            if A[0] == target:
                return 0
            else:
                return -1
        left = 0
        right = lenOfA - 1
        center = (left + right)/2
        while left <= right:
            if left == right:
                if target == A[left]:
                    return left
                else:
                    return -1
            if A[left] < A[right]:
                return binarySearch(A, left, right, target)
            else:
                if center == left:
                    if target == A[center]:
                        return center
                    elif target == A[right]:
                        return right
                    else:
                        return -1
                else:
                    if A[left] < A[center]:
                        if A[left] <= target <= A[center]:
                            return binarySearch(A, left, center, target)
                        else:
                            left = center + 1
                            center = (left + right)/2
                    else:
                        if A[center] <= target <= A[right]:
                            return binarySearch(A, center, right, target)
                        else:
                            right = center - 1
                            center = (left + right)/2
s = Solution()
A = [4,5,6,7,0,1,2]
print s.search(A, 9)