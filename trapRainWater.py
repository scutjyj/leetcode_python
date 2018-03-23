#!/usr/bin/env python
# coding=utf-8

"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if len(height) < 3:
            return 0
        else:
            leftPos = 0
            rightPos = 1
            sumOfWater = 0
            restMax = height[rightPos]
            maxCursor = rightPos
            while leftPos < len(height):
                print '1--lef = %s,rig = %s,sum = %s' % (leftPos, rightPos, sumOfWater)
                if rightPos >= len(height):
                    break
                restMax = height[rightPos]
                maxCursor = rightPos
                while height[leftPos] > height[rightPos]:
                    if height[rightPos] >= restMax:
                        restMax = height[rightPos]
                        maxCursor = rightPos
                    rightPos += 1
                    if rightPos >= len(height):
                        tmpDis = maxCursor - leftPos
                        if tmpDis < 2:
                            leftPos += 1
                            rightPos = leftPos + 1
                            if rightPos >= len(height):
                                leftPos += 2
                                break
                            restMax = height[rightPos]
                            maxCursor = rightPos
                        else:
                            totalVol = height[maxCursor] * (tmpDis + 1)
                            realVol = height[maxCursor]
                            tmpPos = leftPos + 1
                            while tmpPos <= maxCursor:
                                realVol += height[tmpPos]
                                tmpPos += 1
                            sumOfWater = sumOfWater + (totalVol - realVol)
                            leftPos = maxCursor
                            rightPos = leftPos + 1						
                        break
						
                else:
                    print '2--lef = %s,rig = %s,sum = %s' % (leftPos, rightPos, sumOfWater)
                    dis = rightPos - leftPos
                    if dis == 0:
                        rightPos += 1
                    elif dis == 1:
                        leftPos += 1
                        rightPos += 1
                    else:
                        totalVol = height[leftPos] * (dis + 1)
                        realVol = 0
                        tmpPos = leftPos
                        while tmpPos < rightPos:
                            realVol += height[tmpPos]
                            tmpPos += 1
                        else:
                            realVol += height[leftPos]
                        sumOfWater = sumOfWater + (totalVol - realVol)
                        leftPos = rightPos
                        rightPos += 1
            return sumOfWater

s = Solution()
#height = [0,1,0,2,1,0,1,3,2,1,2,1]
#height = [4,2,3]
#height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
height = [1,1,1,1]
print s.trap(height)
			