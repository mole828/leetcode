#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
from tools.TreeNode import TreeNode, TreeBuilder
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def t3c2(t: tuple[int,int,int], v: int) -> tuple[int,int,int]:
            a,b,c = t 
            return (a,v,c)
            
        def dfs(node: Optional[TreeNode], deep: int = 0) -> tuple[int,int,int]:
            if node:
                return max([
                    (deep, 1, node.val), 
                    t3c2(dfs(node.left, deep+1),2), 
                    t3c2(dfs(node.right, deep+1),0),
                ])
            return (-1, -1, -1)
        return dfs(root)[-1]
# @lc code=end

null = None 
print(Solution().findBottomLeftValue(TreeBuilder.build([2,1,3])))
print(Solution().findBottomLeftValue(TreeBuilder.build([1,2,3,4,null,5,6,null,null,7])))