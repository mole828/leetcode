#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sum_of_tree = 0
        def dfs(node: TreeNode, has: str):
            new_has = f"{has}{node.val}"
            if node.left or node.right:
                if node.left:
                    dfs(node.left, new_has)
                if node.right:
                    dfs(node.right, new_has)
            else:
                nonlocal sum_of_tree
                sum_of_tree += int(new_has, base=2)
        dfs(root, "0")
        return sum_of_tree

# @lc code=end

if __name__ == "__main__":
    pass