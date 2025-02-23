#
# @lc app=leetcode id=889 lang=python3
# @lcpr version=30204
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def make() -> TreeNode:
            node = TreeNode(postorder.pop())
            if node.val != preorder[-1]:
                node.right = make()
            if node.val != preorder[-1]:
                node.left = make()
            preorder.pop()
            return node
        return make()

# @lc code=end



#
# @lcpr case=start
# [1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[1]\n
# @lcpr case=end

#

