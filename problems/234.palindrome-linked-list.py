#
# @lc app=leetcode id=234 lang=python3
# @lcpr version=
#
# [234] Palindrome Linked List
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        node = head 
        while node:
            arr.append(node.val)
            node = node.next 
        for i in range(len(arr)):
            if arr[i] != arr[-i-1]:
                return False
        return True
        
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

