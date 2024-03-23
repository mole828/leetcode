#
# @lc app=leetcode id=143 lang=python3
# @lcpr version=
#
# [143] Reorder List
#

from tools.ListNode import ListNode

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr:list[ListNode] = []
        node = head 
        while node:
            arr.append(node)
            node = node.next 
        node = ListNode() 
        pop_i = 0
        while arr: 
            node.next = arr.pop(pop_i) 
            node = node.next 
            node.next = None
            pop_i = -1 - pop_i
        
            

# @lc code=end

head = ListNode.build([1,2,3,4])
print(head)
Solution().reorderList(head)
print(head)

#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#

