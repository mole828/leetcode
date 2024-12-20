#
# @lc app=leetcode id=2415 lang=python3
# @lcpr version=
#
# [2415] Reverse Odd Levels of Binary Tree
#
from tools.TreeNode import TreeNode, TreeBuilder

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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l = root.left
        r = root.right
        visited = set()
        def left_first(node: Optional[TreeNode], deep: int):
            if node:
                if deep%2:
                    yield node
                for n in left_first(node.left, deep=deep+1):
                    yield n
                for n in left_first(node.right, deep=deep+1):
                    yield n
        def right_first(node: Optional[TreeNode], deep: int):
            if node:
                if deep%2:
                    yield node
                for n in right_first(node.right, deep=deep+1):
                    yield n
                for n in right_first(node.left, deep=deep+1):
                    yield n
        node_tup = zip(
            [n for n in left_first(root.left, deep=1)], 
            [n for n in right_first(root.right, deep=1)],
        )
        for a,b in node_tup:
            a.val, b.val = b.val, a.val
        return root
# @lc code=end

print(Solution().reverseOddLevels(root = TreeBuilder.build([2,3,5,8,13,21,34])))

#
# @lcpr case=start
# [2,3,5,8,13,21,34]\n
# @lcpr case=end

# @lcpr case=start
# [7,13,11]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]\n
# @lcpr case=end

#

