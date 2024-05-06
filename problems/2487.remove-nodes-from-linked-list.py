#
# @lc app=leetcode id=2487 lang=python3
# @lcpr version=
#
# [2487] Remove Nodes From Linked List
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
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        next_node = self.removeNodes(head.next)
        if next_node and next_node.val > head.val:
            return next_node
        head.next = next_node
        return head
# @lc code=end



#
# @lcpr case=start
# [5,2,13,3,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n
# @lcpr case=end

#

