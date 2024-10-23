#
# @lc app=leetcode id=2641 lang=python3
# @lcpr version=
#
# [2641] Cousins in Binary Tree II
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
from collections import defaultdict

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ds = defaultdict(int)
        def dfs1(node: TreeNode, depth: int):
            if not node:
                return 0
            v = node.val
            ds[depth] += v
            node.val = dfs1(node.left, depth + 1) + dfs1(node.right, depth + 1)
            return v
        
        def dfs2(node: TreeNode, depth: int):
            if node.left:
                dfs2(node.left, depth + 1)
                node.left.val = ds[depth + 1] - node.val
            if node.right:
                dfs2(node.right, depth + 1)
                node.right.val = ds[depth + 1] - node.val
            node.val = 0

        dfs1(root, 0)
        dfs2(root, 0)
        return root
        
# @lc code=end



#
# @lcpr case=start
# [5,4,9,1,10,null,7]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,2]\n
# @lcpr case=end

#

