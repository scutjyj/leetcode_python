#!/usr/bin/env python
# coding=utf-8

"""
41. First Missing Positive
Problem description:
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

import os
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        tmpSum = 0
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                break
            i += 1
        if nums[i] != 1:
            return 1
        j = i
        while j < len(nums):
            tmpSum += nums[j]
            if tmpSum != (nums[i] + nums[j]) * nums[j] / 2:
                return nums[j - 1] + 1
            j += 1
        return nums[j] + 1
		
s = Solution()
nums = [3,4,-1,1]
print s.firstMissingPositive(nums)
print os.path.dirname(__file__)