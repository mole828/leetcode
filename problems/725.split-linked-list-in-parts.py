#
# @lc app=leetcode id=725 lang=python3
# @lcpr version=
#
# [725] Split Linked List in Parts
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


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        ans: List[ListNode] = [None for i in range(k)]
        ans[0] = root
        for i in range(1, k):
            if ans[i - 1]:
                ans[i] = ans[i - 1].next
        while ans[k - 1]:
            for i in range(k-1):
                ans[k - 1] = ans[k - 1].next
                if not ans[k - 1]:
                    break
                for j in range(i, k - 1):
                    ans[j] = ans[j].next
            if ans[k - 1]:
                ans[k - 1] = ans[k - 1].next
        for i in range(k - 1, 0, -1):
            if ans[i - 1]:
                ans[i] = ans[i - 1].next
                ans[i - 1].next = None
        ans[0] = root
        return ans        

# @lc code=end

print(Solution().splitListToParts(ListNode.build([1, 2, 3]), 5))

#
# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10]\n3\n
# @lcpr case=end

#

