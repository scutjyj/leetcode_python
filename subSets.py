#!/usr/bin/env python
# coding=utf-8

"""
78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
	def Subsets(self, nums):
		if len(nums) == 0:
			return [[]]
		else:
			newList = []
			ret = self.Subsets(nums[:-1])
			import copy
			ori = copy.deepcopy(ret)
			for eachList in ret:
				eachList.append(nums[-1])
			return ori + ret
	
	#Iteratively
	def Subsets1(self, nums):
		res = [[]]
		for num in nums:
			res += [item+[num] for item in res]
		return res
		
	#DFS recursively
	def Subsets2(self, nums):
		res = []
		self.dfs(sorted(nums), 0, [], res)
		return res
		
	def dfs(self, nums, index, path, res):
		res.append(path)
		for i in xrange(index, len(nums)):
			self.dfs(nums, i+1, path+[nums[i]], res)
			
	#Bit Manipulation
	def Subsets3(self, nums):
		res = []
		nums.sort()
		for i in xrange(1<<len(nums)):
			tmp = []
			for j in xrange(len(nums)):
				if i & 1 << j:
					tmp.append(nums[j])
			res.append(tmp)
		return res
			
			
s = Solution()
nums = [1,2,3]
print s.Subsets3(nums)