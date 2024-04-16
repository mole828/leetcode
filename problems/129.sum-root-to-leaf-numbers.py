#
# @lc app=leetcode id=129 lang=python3
# @lcpr version=
#
# [129] Sum Root to Leaf Numbers
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0 
        def dfs(node: TreeNode, has: int): 
            new_has = has*10 + node.val
            if node.left or node.right:
                if node.left: 
                    dfs(node.left, new_has) 
                if node.right:
                    dfs(node.right, new_has) 
            else: 
                nonlocal total_sum 
                total_sum += new_has 
        dfs(root, 0) 
        return total_sum
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,0,5,1]\n
# @lcpr case=end

#

