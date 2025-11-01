#
# @lc app=leetcode id=3217 lang=python3
# @lcpr version=
#
# [3217] Delete Nodes From Linked List Present in Array
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
from typing import List, Optional

# same +1
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        begin = ListNode()
        begin.next = head
        this = begin
        while this.next:
            if this.next.val in nums:
                this.next = this.next.next
            else:
                this = this.next
        return begin.next
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n[1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[1,2,1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [5]\n[1,2,3,4]\n
# @lcpr case=end

#

