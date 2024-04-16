#
# @lc app=leetcode id=623 lang=python3
# @lcpr version=
#
# [623] Add One Row to Tree
#


# @lcpr-template-start

# @lcpr-template-end

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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: 
            return TreeNode(val, root)
        def dfs(node: Optional[TreeNode], deep: int): 
            new_deep = deep + 1 
            if node.left: 
                dfs(node.left, new_deep) 
            if node.right: 
                dfs(node.right, new_deep) 
            if new_deep == depth:
                node.left = TreeNode(val, node.left) 
                node.right = TreeNode(val, None, node.right) 
        dfs(root, 1)
        return root 
# @lc code=end

from tools.TreeNode import TreeBuilder
print(Solution().addOneRow(TreeBuilder.build([4,2,6,3,1,5]),1,2))
print(Solution().addOneRow(TreeBuilder.build([4,2,None,3,1]),1,3))

#
# @lcpr case=start
# [4,2,6,3,1,5]\n1\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,2,null,3,1]\n1\n3\n
# @lcpr case=end

#

