#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
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
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        while head:
            ans<<=1
            ans+=head.val
            head = head.next
        return ans
        
# @lc code=end

