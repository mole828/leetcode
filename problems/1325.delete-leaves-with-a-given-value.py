#
# @lc app=leetcode id=1325 lang=python3
# @lcpr version=
#
# [1325] Delete Leaves With a Given Value
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
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def is_leaf(node: Optional[TreeNode]) -> bool:
            return not (node.left or node.right)
        def remove_leaf(node: Optional[TreeNode]):
            if not node:
                return 0
            remove_count = 0
            if node.left and is_leaf(node.left) and node.left.val == target:
                node.left = None
                remove_count += 1
            else:
                remove_count += remove_leaf(node.left)
            if node.right and is_leaf(node.right) and node.right.val == target:
                node.right = None 
                remove_count += 1
            else:
                remove_count += remove_leaf(node.right)
            return remove_count
        # print(root)
        while remove_leaf(root):
            pass
        if is_leaf(root) and root.val == target:
            return None
        # print(root)
        return root     

# @lc code=end

print(Solution().removeLeafNodes(TreeBuilder.build([1,2,3,2,None,2,4]), 2))

#
# @lcpr case=start
# [1,2,3,2,null,2,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,3,3,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,null,2,null,2]\n2\n
# @lcpr case=end

#

