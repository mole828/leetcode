#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

from tools.TreeNode import TreeNode,TreeBuilder
# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        pointer = [0]
        def deep(node: Optional[TreeNode]) -> int:
            if node:
                da, db = deep(node.left), deep(node.right) 
                pointer[0] = max(pointer[0], da+db)
                return max(da,db)+1 
            return 0 
        deep(root)
        return pointer[0]
# @lc code=end

print(Solution().diameterOfBinaryTree(TreeBuilder.build([1,2,3,4,5])))