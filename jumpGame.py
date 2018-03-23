#!/usr/bin/env python
# coding=utf-8

"""
55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

import time

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        """
        #exceed recursive deepth
        
        return self.foobar(nums, 0, len(nums))
    
    def foobar(self, nums, headIndex, length):
        if length <= 1:
            return True
        if nums[headIndex] == 0:
            return False
        if nums[headIndex] >= length - 1:
            return True
        else:
            i = 1
            while i <= nums[headIndex]:
                tmp = self.foobar(nums, headIndex + i, length - i)
                #tmp = self.canJump(nums[i:])
                if tmp:
                    return True
                #else:
                #    nums[headIndex] = 0
                i += 1
            nums[headIndex] = 0
            return False
        """
        numsLen = len(nums)
        if numsLen <= 1:
            return True
        i = 0
        while i < numsLen:
            if nums[i] == 0:
                if i != 0:
                    j = i - 1
                    count = 0
                    while j >= 0:
                        if nums[j] <= i - j:
                            count += 1
                        j -= 1
                    if count == i:
                        if i == numsLen - 1:
                            return True
                        return False
                else:
                    return False
            i += 1
        return True
			
s = Solution()
#nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
#nums = [5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8]
#nums = [3,0,8,2,0,0,1]
#nums = [2,0,0]
nums = [0 for i in range(200)]
nums.insert(0, 201)
print nums
begin = time.time()
print s.canJump(nums)
run_time = time.time() - begin
print 'run_time = %f' % run_time