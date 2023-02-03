from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        lsz = rsz = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            ls = dfs(node.left)
            rs = dfs(node.right)
            if node.val == x:
                nonlocal lsz, rsz
                lsz, rsz = ls, rs
            return ls + rs + 1
        dfs(root)
        return max(lsz, rsz, n - 1 - lsz - rsz) * 2 > n
