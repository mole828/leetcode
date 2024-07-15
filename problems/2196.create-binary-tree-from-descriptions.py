#
# @lc app=leetcode id=2196 lang=python3
# @lcpr version=
#
# [2196] Create Binary Tree From Descriptions
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
from typing import List, Optional


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        son_set: set[int] = set()
        nodes: dict[int, TreeNode] = {}
        for parent,child,isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            parent_node = nodes[parent]
            if child not in nodes:
                nodes[child] = TreeNode(child)
            child_node = nodes[child]
            son_set.add(child)
            if isLeft:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        sum_set = set(nodes.keys())
        root = (sum_set - son_set).pop()
        return nodes[root]

# @lc code=end

print(Solution().createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))

#
# @lcpr case=start
# [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,1],[2,3,0],[3,4,1]]\n
# @lcpr case=end

#

