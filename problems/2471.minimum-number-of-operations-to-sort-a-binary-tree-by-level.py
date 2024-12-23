#
# @lc app=leetcode id=2471 lang=python3
# @lcpr version=
#
# [2471] Minimum Number of Operations to Sort a Binary Tree by Level
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


# link https://leetcode.cn/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/solutions/1965422/by-endlesscheng-97i9/

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans, next_row = 0, [root]
        while next_row:
            this_row_value = []
            this_row = next_row
            next_row = []
            for node in this_row:
                this_row_value.append(node.val)
                if node.left: next_row.append(node.left)
                if node.right: next_row.append(node.right)

            n = len(this_row_value)
            this_row_index = sorted(range(n), key=lambda i: this_row_value[i])  # 离散化

            ans += n
            visted = [False] * n
            for v in this_row_index:
                if visted[v]: continue
                while not visted[v]:
                    visted[v] = True
                    v = this_row_index[v]
                ans -= 1
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,4,3,7,6,8,5,null,null,null,null,9,null,10]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2,7,6,5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n
# @lcpr case=end

#

