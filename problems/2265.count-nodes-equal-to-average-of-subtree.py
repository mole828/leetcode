#
# @lc app=leetcode id=2265 lang=python3
#
# [2265] Count Nodes Equal to Average of Subtree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        _sum = [0]
        def dfs(node: Optional[TreeNode]) -> tuple[int,int]:
            '''
            :return node_num node_sum
            '''
            if node:
                nn0,ns0 = dfs(node.left)
                nn1,ns1 = dfs(node.right)
                nn = sum([1,nn0,nn1])
                ns = sum([node.val,ns0,ns1])
                avg = ns//nn
                if node.val == avg:
                    _sum[0] += 1
                # print(node.val, nn, ns, avg)
                return nn,ns
            else:
                return 0,0
        dfs(root)
        return _sum[0]

# @lc code=end

