#
# @lc app=leetcode id=206 lang=python3
# @lcpr version=
#
# [206] Reverse Linked List
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        def reverseList(head: Optional[ListNode]) -> tuple[ListNode,ListNode]:
            print(head, not head.next)
            if not head.next:
                return (head, head)
            left, right = reverseList(head.next)
            head.next = None 
            right.next = head 
            return left,head
        left, right = reverseList(head)
        return left

        
# @lc code=end

print(Solution().reverseList(ListNode.build([1,2,3,4,5])))

#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

