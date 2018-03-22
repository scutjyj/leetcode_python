#!/usr/bin/env python
# coding=utf-8

"""
40. Combination Sum II

Given a collection of candidate numbers (C) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        ret = []
        if len(candidates) == 0:
            return ret
        elif len(candidates) == 1:
            if target == candidates[0]:
                ret.append(candidates)
            return ret
        else:
            #print candidates, target
            lastRet = self.combinationSum2(candidates[:-1], target)
            #print 'lastRet=%s' % lastRet
            if target == candidates[-1]:
                if [candidates[-1]] not in lastRet:
                    lastRet.append([candidates[-1]])
                return lastRet
            if target - candidates[-1] > 0:
               tmpRet = self.combinationSum2(candidates[:-1], target - candidates[-1])
               #print 'tmpRet=%s' % tmpRet
               if len(tmpRet) != 0:
                   for eachList in tmpRet:
                       eachList.append(candidates[-1])
                   for eachList in tmpRet:
                       if eachList not in lastRet:
                           lastRet.append(eachList)
            return lastRet

s = Solution()
#candidates = [10,1,2,7,6,1,5,2,4]
#target = 8
#candidates = [1,1,2,2,4]
#target = 4
candidates = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
target = 27
print s.combinationSum2(candidates, target)