#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

from tools.TreeNode import TreeNode

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.

from collections import defaultdict
from typing import List, Optional


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        rows_max = defaultdict(lambda:-1<<32) # -2^31 <= Node.val <= 2^31 - 1
        def dfs(node: Optional[TreeNode], deep: int):
            if node:
                rows_max[deep] = max(rows_max[deep], node.val)
                dfs(node.left, deep+1)
                dfs(node.right, deep+1)
        dfs(root, 0)
        return [v for v in rows_max.values()]
        
# @lc code=end

