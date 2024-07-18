#
# @lc app=leetcode id=1530 lang=python3
# @lcpr version=
#
# [1530] Number of Good Leaf Nodes Pairs
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
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        pointer = [0]
        def dfs(node: TreeNode):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            for i in left:
                for j in right:
                    if i+j <= distance:
                        pointer[0] += 1
            return [i+1 for i in left+right if i+1 < distance]
        dfs(root)
        return pointer[0]
# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [7,1,4,6,null,5,3,null,null,null,null,null,2]\n3\n
# @lcpr case=end

#

