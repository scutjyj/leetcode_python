#!/usr/bin/env python
# coding=utf-8

"""
39. Combination Sum

Given a set of candidate numbers (C) (without duplicates) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        #print candidates, target
        ret = []
        if len(candidates) == 0:
            return ret
        elif len(candidates) == 1:
            if target % candidates[0] == 0:
                i = 0
                tmp = []
                while i < target/candidates[0]:
                    tmp.append(candidates[0])
                    i += 1
                ret = [tmp]
            return ret
        else:
            lastRet = self.combinationSum(candidates[:-1], target)
            #print 'lastRet = %s' % (lastRet,)
            i = 1
            while i <= target/candidates[-1]:
                if i * candidates[-1] == target:
                    lastRet.append([candidates[-1] for j in range(i)])
                    break
                if i * candidates[-1] < target:
                    tmpRet = self.combinationSum(candidates[:-1], target - i * candidates[-1])
                    if len(tmpRet) != 0:
                        #print tmpRet
                        for eachList in tmpRet:
                            eachList.extend([candidates[-1] for j in range(i)])
                        lastRet.extend(tmpRet)
                i += 1
            return lastRet
			
s = Solution()
candidates = [2,3,6,7]
target = 7
print s.combinationSum(candidates, target)