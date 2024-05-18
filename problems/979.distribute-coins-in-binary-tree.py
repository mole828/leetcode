#
# @lc app=leetcode id=979 lang=python3
# @lcpr version=
#
# [979] Distribute Coins in Binary Tree
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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            self.moves += abs(left) + abs(right)
            return node.val + left + right - 1
        
        self.moves = 0
        dfs(root)
        return self.moves
# @lc code=end



#
# @lcpr case=start
# [3,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,0]\n
# @lcpr case=end

#

