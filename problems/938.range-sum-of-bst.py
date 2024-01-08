#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            return sum([
                root.val if low <= root.val <= high else 0, 
                self.rangeSumBST(root.left, low, high), 
                self.rangeSumBST(root.right, low, high)
            ])
        return 0
# @lc code=end

