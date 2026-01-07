#
# @lc app=leetcode id=1339 lang=python3
#
# [1339] Maximum Product of Splitted Binary Tree
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sum_cache = {}
        def dfs_sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            if node in sum_cache:
                return sum_cache[node]
            total = node.val + dfs_sum(node.left) + dfs_sum(node.right)
            sum_cache[node] = total
            return total
        total_sum = dfs_sum(root)
        # print(sum_cache)
        max_product = 0
        for node in sum_cache:
            part_sum = sum_cache[node]
            other_part_sum = total_sum - part_sum
            product = part_sum * other_part_sum
            if product > max_product:
                max_product = product
                # print(other_part_sum, part_sum, node)

        return max_product % (10**9 + 7)
        
# @lc code=end

if __name__ == "__main__":
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print(Solution().maxProduct(root))