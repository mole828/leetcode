#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

from typing import Optional
from tools.TreeNode import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], v_min: int, v_max: int) -> int:
            if node:
                diff = max(abs(v_min-node.val), abs(v_max-node.val))
                v_min = min(v_min, node.val)
                v_max = max(v_max, node.val)
                d_left = dfs(node.left, v_min, v_max)
                d_right = dfs(node.right, v_min, v_max)
                return max(diff, d_left, d_right)
            return - float('inf')
        return dfs(root, root.val, root.val)
                
# @lc code=end

