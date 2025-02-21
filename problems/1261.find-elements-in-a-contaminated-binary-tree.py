#
# @lc app=leetcode id=1261 lang=python3
#
# [1261] Find Elements in a Contaminated Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class FindElements:
    has: set[int]
    def __init__(self, root: Optional[TreeNode]):
        self.has = set()
        def dfs(node: Optional[TreeNode], val: int):
            if node is None:
                return
            node.val = val
            self.has.add(val)
            dfs(node.left, 2 * val + 1)
            dfs(node.right, 2 * val + 2)
        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.has

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end

