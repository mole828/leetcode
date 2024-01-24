#
# @lc app=leetcode id=1457 lang=python3
#
# [1457] Pseudo-Palindromic Paths in a Binary Tree
#
# Definition for a binary tree node.
class TreeNode:
    val: int 
    left: 'TreeNode'
    right: 'TreeNode'
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode):
        count = 0
        stack = [(root, 0)]

        while stack:
            node, path = stack.pop()

            if node:
                path ^= 1 << node.val

                if not node.left and not node.right:
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))

        return count


# @lc code=end

