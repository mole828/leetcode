#
# @lc app=leetcode id=1609 lang=python3
#
# [1609] Even Odd Tree
#

from tools.TreeNode import TreeBuilder, TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        rows = {}
        def dfs(node: Optional[TreeNode], deep: int):
            if node:
                if deep%2:
                    if deep not in rows:
                        rows[deep] = float('inf')
                    if node.val >= rows[deep] or (node.val)%2:
                        print({
                            'deep': deep,
                            'rows[deep]': rows[deep],
                            'node.val': node.val
                        })
                        raise ValueError
                else:
                    if deep not in rows:
                        rows[deep] = float('-inf')
                    if node.val <= rows[deep] or (node.val+1)%2:
                        print({
                            'deep': deep,
                            'rows[deep]': rows[deep],
                            'node.val': node.val
                        })
                        raise ValueError
                rows[deep] = node.val
                dfs(node.left, deep+1)
                dfs(node.right, deep+1)
        try:
            dfs(root, 0)
        except:
            return False
        return True
        
# @lc code=end
null = None
print(Solution().isEvenOddTree(TreeBuilder.build([1,10,4,3,null,7,9,12,8,6,null,null,2])))