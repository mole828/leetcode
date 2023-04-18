# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

from sortedcontainers import SortedList


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        pats = SortedList([root.val])
        def dfs(node:Optional[TreeNode], pat:SortedList[int]) -> int:
            if node is None:return -1
            ans = [ abs(node.val-pat[0]), abs(node.val-pat[-1]) ]
            pat.add(node.val)
            ans.append(dfs(node.left, pat))
            ans.append(dfs(node.right, pat))
            pat.remove(node.val)
            return max(ans)
        return max(dfs(root.left,pats),dfs(root.right,pats))