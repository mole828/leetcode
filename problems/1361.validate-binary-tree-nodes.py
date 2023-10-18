#
# @lc app=leetcode id=1361 lang=python3
#
# [1361] Validate Binary Tree Nodes
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        children = set(leftChild) | set(rightChild)
        allnode = set([i for i in range(n)])
        without_in_degree = allnode - children
        if len(without_in_degree) != 1:
            return False
        root = without_in_degree.pop()
        stack = [root]
        seen = {root}
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False
                    stack.append(child)
                    seen.add(child)
        return seen == allnode

# @lc code=end

print(Solution().validateBinaryTreeNodes(
    4,
    [1, -1, 3, -1],
    [2, 3, -1, -1],
))

print(Solution().validateBinaryTreeNodes(
    4,
    [1, -1, 3, -1],
    [2, -1, -1, -1],
))
