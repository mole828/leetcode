#
# @lc app=leetcode id=951 lang=python3
# @lcpr version=
#
# [951] Flip Equivalent Binary Trees
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
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def isflip(curnode1,curnode2):
            if not curnode1 and not curnode2:
                return True
            
            if not curnode1 and curnode2:
                return False
            if curnode1 and not curnode2:
                return False
            
            if curnode1.val==curnode2.val:
                return (isflip(curnode1.left,curnode2.left) and isflip(curnode1.right,curnode2.right)) or (isflip(curnode1.left,curnode2.right) and isflip(curnode1.right , curnode2.left))
            else:
                return False
        
        return isflip(root1,root2)

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,null,null,null,7,8]\n[1,3,2,null,6,4,5,null,null,null,null,8,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[1]\n
# @lcpr case=end

#

