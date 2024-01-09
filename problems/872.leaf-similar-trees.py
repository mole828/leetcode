#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]):
            if node:
                is_leaf = True
                for leaf in dfs(node.left):
                    is_leaf = False
                    yield leaf 
                for leaf in dfs(node.right):
                    is_leaf = False
                    yield leaf 
                if is_leaf:
                    yield node.val
        
        return [x for x in dfs(root1)] == [x for x in dfs(root2)]
            
# @lc code=end

a = TreeNode(val=1, left=TreeNode(2), right=TreeNode(3))
b = TreeNode(val=1, left=TreeNode(3), right=TreeNode(2))
print(Solution().leafSimilar(a,b))