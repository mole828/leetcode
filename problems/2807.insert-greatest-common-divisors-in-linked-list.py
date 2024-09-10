#
# @lc app=leetcode id=2807 lang=python3
# @lcpr version=
#
# [2807] Insert Greatest Common Divisors in Linked List
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
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        p = head
        while p.next:
            p.next = ListNode(self.gcd(p.val,p.next.val),p.next)
            p = p.next.next
        return head
    
    def gcd(self,a,b):
        if b == 0:
            return a
        return self.gcd(b,a%b)
        
# @lc code=end



#
# @lcpr case=start
# [18,6,10,3]\n
# @lcpr case=end

# @lcpr case=start
# [7]\n
# @lcpr case=end

#

