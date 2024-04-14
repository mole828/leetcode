#
# @lc app=leetcode id=404 lang=python3
# @lcpr version=
#
# [404] Sum of Left Leaves
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
from collections import deque



class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 
        queue = deque([(root,False)]) 
        total_sum = 0 
        while queue: 
            node, is_left = queue.popleft() 
            if is_left and not node.left and not node.right: 
                total_sum += node.val 
            if node.left: 
                queue.append((node.left, True))
            if node.right: 
                queue.append((node.right, False))
        return total_sum 
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

