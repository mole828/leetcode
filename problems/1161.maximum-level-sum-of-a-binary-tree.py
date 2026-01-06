#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

from collections import defaultdict
from tools.TreeNode import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels_sums = defaultdict(int)
        def dfs(node: Optional[TreeNode], level: int):
            if not node:
                return
            if level not in levels_sums:
                levels_sums[level] = 0
            levels_sums[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 1)
        return max(levels_sums, key=levels_sums.get)
# @lc code=end

