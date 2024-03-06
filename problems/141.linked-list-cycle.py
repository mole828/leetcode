#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

from tools.ListNode import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = [] 
        node = head 
        while node:
            if node in nodes:
                return True
            nodes.append(node)
            node = node.next
        return False
        
# @lc code=end

