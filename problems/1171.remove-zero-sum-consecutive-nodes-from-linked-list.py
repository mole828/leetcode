#
# @lc app=leetcode id=1171 lang=python3
# @lcpr version=
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#


# @lcpr-template-start

# @lcpr-template-end

from tools.ListNode import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sums = {0: dummy}
        current = head

        while current:
            # print(head, prefix_sums)
            prefix_sum += current.val
            if prefix_sum in prefix_sums:
                to_delete = prefix_sums[prefix_sum].next
                temp_sum = prefix_sum + to_delete.val
                while to_delete != current:
                    del prefix_sums[temp_sum]
                    to_delete = to_delete.next
                    temp_sum += to_delete.val
                prefix_sums[prefix_sum].next = current.next
            else:
                prefix_sums[prefix_sum] = current
            current = current.next

        return dummy.next
        


        
        
        

        
# @lc code=end

print(Solution().removeZeroSumSublists(ListNode.build([1,2,1,-3,3])))

#
# @lcpr case=start
# [1,2,-3,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,-3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,-3,-2]\n
# @lcpr case=end

#

