#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True 
        elif p and q and p.val == q.val:
            return all([
                self.isSameTree(p.left, q.left),
                self.isSameTree(p.right,q.right)
            ])
        else:
            return False

# @lc code=end

