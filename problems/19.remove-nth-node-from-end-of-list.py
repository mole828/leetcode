#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

from tools.ListNode import ListNode 

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = ListNode(None, head)
        def lastOf(node: Optional[ListNode]) -> int:
            if node:
                last = lastOf(node.next)
                if last == n:
                    node.next = node.next.next
                return last + 1
            return 0
        lastOf(front)
        return front.next
        
# @lc code=end

print(Solution().removeNthFromEnd(ListNode.build([1,2,3,4,5]), 2))