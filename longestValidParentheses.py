#!/usr/bin/env python
# coding=utf-8

"""32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        tmpStack = []
        maxLen = tmpLen = 0
        if len(s) == 0:
            return 0
        for eachChar in s:
            if eachChar == '(':
                tmpStack.append(eachChar)
            elif len(tmpStack) == 0:
                tmpStack.append(eachChar)
            else:
                i = len(tmpStack) - 1
                while i >= 0:
                    if tmpStack[i] == '(':
                        if i == len(tmpStack) - 1:
                            toBePushed = 2
                            tmpStack.pop()
                            if len(tmpStack) == 0:
                                tmpStack.append(toBePushed)
                                break
                            if tmpStack[-1] != '(' and tmpStack[-1] != ')':
                                toBePushed += tmpStack[-1]
                                tmpStack.pop()
                            tmpStack.append(toBePushed)
                            break
                        else:
                            toBePushed = tmpStack[i+1] + 2
                            tmpStack.pop()  #pop the num
                            tmpStack.pop()  #pop the '('
                            if len(tmpStack) == 0:
                                tmpStack.append(toBePushed)
                                break
                            if tmpStack[-1] != '(' and tmpStack[-1] != ')':
                                toBePushed += tmpStack[-1]
                                tmpStack.pop()
                            tmpStack.append(toBePushed)
                            break
                    else:
                        i -= 1
                else:
                    tmpStack.append(eachChar)
        i = 0
        while i < len(tmpStack):
            if tmpStack[i] != '(' and tmpStack[i] != ')':
                if tmpStack[i] > maxLen:
                    maxLen = tmpStack[i]
            i += 1
        return maxLen

s = Solution()
astr = "()(()(()()"
print s.longestValidParentheses(astr)