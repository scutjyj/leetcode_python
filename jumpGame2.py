#!/usr/bin/env python
# coding=utf-8

"""
45. Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2.
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) <= 1:
            return 0
        numsLen = len(nums)
        jmpNum = [-1 for i in range(numsLen - 1)]
        jmpNum.append(0)
        i = 1
        while jmpNum[0] == -1:
            j = numsLen - 2
            while j >= 0:
                if jmpNum[j] == -1:
                    k = j+1
                    print i,j
                    while jmpNum[k] != i - 1:
                        print k
                        k += 1
                    if k == j+1:
                        jmpNum[j] = i
                    else:
                        if nums[j] >= k - j:
                            jmpNum[j] = i
                j -= 1
            i += 1
        return jmpNum[0]
		
s = Solution()
nums = [1,1,1,1]
#nums = [2,3,1,1,4]
print s.jump(nums)