#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    next: 'ListNode'
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None 
        if not l1:
            l1 = ListNode(0)
        if not l2:
            l2 = ListNode(0)
            
        val= l1.val + l2.val
        if val>9:
            val -= 10
            if l1.next:
                l1.next.val += 1
            elif l2.next:
                l2.next.val += 1
            else:
                l1.next = ListNode(1)
        nextNode = self.addTwoNumbers(l1.next, l2.next)
        node = ListNode(
            val= val,
            next= nextNode,
        )
        return node
# @lc code=end

