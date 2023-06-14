# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ns = set()
        ans = [float('inf')]

        def add(x):
            for n in ns:
                if abs(n-x) < ans[0]:
                    ans[0] = abs(n-x)
            ns.add(x)

        def dfs(node):
            if node:
                print(node)
                add(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return int(ans[0])
