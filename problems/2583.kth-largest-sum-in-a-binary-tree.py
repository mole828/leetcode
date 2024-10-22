#
# @lc app=leetcode id=2583 lang=python3
# @lcpr version=
#
# [2583] Kth Largest Sum in a Binary Tree
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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode], level: int):
            if not node:
                return
            if level < len(levels):
                levels[level] += node.val
            else:
                levels.append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        levels = []
        dfs(root, 0)
        if len(levels) < k:
            return -1
        levels.sort()
        return levels[-k]
        
# @lc code=end



#
# @lcpr case=start
# [5,8,9,2,1,3,7,4,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,null,3]\n1\n
# @lcpr case=end

#

