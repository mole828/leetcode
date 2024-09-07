#
# @lc app=leetcode id=1367 lang=python3
# @lcpr version=
#
# [1367] Linked List in Binary Tree
#

from functools import cache
from tools.ListNode import ListNode
from tools.TreeNode import TreeNode

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        @cache
        def dfs(list_node: ListNode, tree_node: TreeNode) -> bool:
            if not list_node:
                return True
            if not tree_node:
                return False
            if list_node.val == tree_node.val:
                if dfs(list_node.next, tree_node.left) or dfs(list_node.next, tree_node.right):
                    return True
                # if head.val == tree_node.val:
                #     return dfs(head.next, tree_node.left) or dfs(head.next, tree_node.right)
            if head.val == tree_node.val:
                return dfs(head.next, tree_node.left) or dfs(head.next, tree_node.right)
            return dfs(head, tree_node.left) or dfs(head, tree_node.right)

        return dfs(head, root)
# @lc code=end



#
# @lcpr case=start
# [4,2,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,6]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,6,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\n
# @lcpr case=end

#

