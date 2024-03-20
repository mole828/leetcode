#
# @lc app=leetcode id=1669 lang=python3
# @lcpr version=
#
# [1669] Merge In Between Linked Lists
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


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        nodeA = list1
        nodeB = list1 
        a -= 1 
        while a:
            nodeA = nodeA.next
            a -= 1
        while b:
            nodeB = nodeB.next
            b -= 1
        nodeA.next = list2 
        end = list1 
        while end.next:
            end = end.next
        end.next = nodeB.next
        return list1
        
# @lc code=end

print(Solution().mergeInBetween(list1 = ListNode.build([10,1,13,6,9,5]), a = 3, b = 4, list2 = ListNode.build([1000000,1000001,1000002])))

#
# @lcpr case=start
# [10,1,13,6,9,5]\n3\n4\n[1000000,1000001,1000002]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,3,4,5,6]\n2\n5\n[1000000,1000001,1000002,1000003,1000004]\n
# @lcpr case=end

#

