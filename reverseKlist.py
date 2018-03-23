#!/usr/bin/env python
# coding=utf-8

"""
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head is None:
            return None
        if k == 1:
            return head
        ptr = head
        ret = lastEnd = nextHead = head
        isFirst = 1
        cnt = 0
        while True:
            ptr = nextHead
            tmpHead = nextHead
            tmpEnd = nextHead
            cnt = 0
            while cnt < k:
                if ptr is None:
                    print ptr
                    break
                cnt += 1
                tmpEnd = ptr
                ptr = ptr.next
            if cnt < k:
                #TODO
                break
            else:
                nextHead = ptr
            bef = tmpHead
            now = tmpHead.next
            print bef.val, now.val
            print "Hello,world"
            #while now.next is not None and now is not tmpEnd.next:
            i = 1
            while i < k:
                print now.next
                aft = now.next
                now.next = bef
                bef = now
                now = aft
                i += 1
            if isFirst == 1:
                ret = tmpEnd
                tmpHead.next = nextHead
                isFirst = 0
            else:
                #TODO
                lastEnd.next = tmpEnd
            lastEnd = tmpHead
        if isFirst == 0:
            lastEnd.next = nextHead
        return ret

slt = Solution()
nodeList = []
k = 2
for eachNum in [1]:
    nodeList.append(ListNode(eachNum))
i = 0
while i < len(nodeList) - 1:
    nodeList[i].next = nodeList[i+1]
    i += 1
else:
    nodeList[i].next = None
ptr = nodeList[0]
ret = slt.reverseKGroup(nodeList[0], k)
while ret is not None:
    print ret.val,
    ret = ret.next
#for eachNode in nodeList:
#    print eachNode.val,
