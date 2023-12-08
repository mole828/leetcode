#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root:
            output = str(root.val)
            left = self.tree2str(root.left)
            right = self.tree2str(root.right)
            if left:
                output += f"({left})"
            if right:
                if not left:
                    output += "()"
                output += f"({right})"
            return output
        return ''
# @lc code=end

