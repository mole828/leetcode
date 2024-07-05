#
# @lc app=leetcode id=2181 lang=python3
# @lcpr version=
#
# [2181] Merge Nodes in Between Zeros
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
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        znode = ListNode()
        zhead = znode
        node = head 
        total = 0
        while node:
            if node.val == 0:
                znode.next = ListNode(total)
                znode = znode.next
                total = 0
            else:
                total += node.val
            node = node.next
        return zhead.next.next
# @lc code=end

print(Solution().mergeNodes(ListNode.build([0,3,1,0,4,5,2,0])))

#
# @lcpr case=start
# [0,3,1,0,4,5,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,0,2,2,0]\n
# @lcpr case=end

#

