#
# @lc app=leetcode id=2331 lang=python3
# @lcpr version=
#
# [2331] Evaluate Boolean Binary Tree
#

from tools.TreeNode import TreeNode
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root:
            if root.val == 0:
                return False
            if root.val == 1:
                return True
            if root.val == 2:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            if root.val == 3:
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        return False
# @lc code=end



#
# @lcpr case=start
# [2,1,3,null,null,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

