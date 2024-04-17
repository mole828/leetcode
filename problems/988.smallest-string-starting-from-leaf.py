#
# @lc app=leetcode id=988 lang=python3
# @lcpr version=
#
# [988] Smallest String Starting From Leaf
#


# @lcpr-template-start

# @lcpr-template-end

from typing import Optional
from tools.TreeNode import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        min_ls = [float('inf')]
        def dfs(node: Optional[TreeNode], ls = []) -> list:
            is_leaf = not any([node.left, node.right]) 
            new_ls = [node.val] + ls 
            if is_leaf:
                nonlocal min_ls
                if new_ls < min_ls:
                    min_ls = new_ls 
                return 
            if node.left: 
                dfs(node.left, new_ls)
            if node.right: 
                dfs(node.right, new_ls)
        dfs(root)
        return ''.join(chr(x+ord('a')) for x in min_ls)
        
# @lc code=end



#
# @lcpr case=start
# [0,1,2,3,4,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [25,1,3,1,3,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,null,1,0,null,0]\n
# @lcpr case=end

#

