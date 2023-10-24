#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict
from typing import List, Optional


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        rows_max = defaultdict(lambda:-1<<32)
        def dfs(node: Optional[TreeNode], deep: int):
            if node:
                rows_max[deep] = max(rows_max[deep], node.val)
                dfs(node.left, deep+1)
                dfs(node.right, deep+1)
        dfs(root, 0)
        return [v for v in rows_max.values()]
        
# @lc code=end

