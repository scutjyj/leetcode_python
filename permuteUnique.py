#!/usr/bin/env python
# coding: utf-8

"""
47. Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        """
        l = len(nums)
        if l == 0:
            return []
        elif l == 1:
            return [nums]
        else:
            rst = []
            lastList = self.permuteUnique(nums[:-1])
            for eachList in lastList:
                i = 0
                ll = len(eachList)
                while i <= ll:
                    temp = eachList[::]
                    temp.insert(i, nums[-1])
                    rst.append(temp)
                    i += 1
            ret = []
            for eachList in rst:
                if eachList not in ret:
                    ret.append(eachList)
            return ret
        """
        
        """
        # The code below is using itering method and is faster that the code above.
        num_dict = {}
        for i in nums:
            k = str(i)
            num_dict[k] = num_dict.get(k, 0) + 1
        l = len(nums)
        return self.iter_func(num_dict)
        """
        
        # reference answer.
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break              #handles duplication
            ans = new_ans
        return ans
    
    def iter_func(self, num_dict):
        ret = []
        #print num_dict
        if num_dict:
            
            ks = num_dict.keys()
            if len(ks) == 1:
                ret = [[int(ks[0]) for i in range(num_dict[ks[0]])]]
                #print 'ret= ', ret
                return ret
            
            for k,v in num_dict.iteritems():
                tmp_dict = num_dict.copy()
                tmp_dict[k] -= 1
                if not tmp_dict[k]:
                    tmp_dict.pop(k)
                tmp_ret = self.iter_func(tmp_dict)
                for eachList in tmp_ret:
                    eachList.insert(0, int(k))
                #print v, tmp_ret
                ret.extend(tmp_ret)
            return ret
        else:
            return [[]]

if __name__ == '__main__':
    s = Solution()
    t = [1,1,2]
    print s.permuteUnique(t)
    
 
