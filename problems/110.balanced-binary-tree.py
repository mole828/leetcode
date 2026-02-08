#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(node: Optional[TreeNode]) -> int:
            """返回以node为根的子树的高度"""
            nonlocal balanced
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if abs(left_height - right_height) > 1:
                balanced = False
            return max(left_height, right_height) + 1
        dfs(root)
        return balanced
        
# @lc code=end

