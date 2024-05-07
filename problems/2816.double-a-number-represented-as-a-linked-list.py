#
# @lc app=leetcode id=2816 lang=python3
# @lcpr version=
#
# [2816] Double a Number Represented as a Linked List
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
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def double_it(node: Optional[ListNode]) -> int:
            if node:
                new_val = node.val * 2 + double_it(node.next)
                node.val = new_val%10
                return new_val//10
            return 0
        i = double_it(head)
        if i:
            head = ListNode(val=i, next=head)
        return head
        
# @lc code=end



#
# @lcpr case=start
# [1,8,9]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9]\n
# @lcpr case=end

#

