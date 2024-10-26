#
# @lc app=leetcode id=2458 lang=python3
# @lcpr version=
#
# [2458] Height of Binary Tree After Subtree Removal Queries
#

from collections import defaultdict
from functools import cache
import heapq
from tools.TreeNode import TreeNode, TreeBuilder

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

# Time Limit Exceeded, 30 / 40 testcases passed
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def copy_tree(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            new_node = TreeNode(node.val)
            new_node.left = copy_tree(node.left)
            new_node.right = copy_tree(node.right)
            return new_node

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1

        def remove(node: Optional[TreeNode], val: int) -> bool:
            if not node:
                return False
            if node.left and node.left.val == val:
                node.left = None
                return True
            if node.right and node.right.val == val:
                node.right = None
                return True
            if remove(node.left, val): return True
            if remove(node.right, val): return True
            return False

        result = []
        for val in queries:
            new_root = copy_tree(root)
            remove(new_root, val)
            h = height(new_root)
            result.append(h-1)
        return result


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        levels = defaultdict(list)
        def dfs(node: Optional[TreeNode],lvl):
            if not node:
                return 0
            height = max(dfs(node.left,lvl+1),dfs(node.right,lvl+1))+1
            levels[lvl].append((height,node.val))
            return height

        root_height = dfs(root,0) -1

        highest_nodes = {}
        for lvl in levels.values():
            if len(lvl) == 1:
                highest,next = lvl[0],(0,0)
            else:
                highest,next = heapq.nlargest(2, lvl)
            highest_nodes[highest[1]] = (highest[0],next[0])

        result = []
        for q in queries:
            deleted_height,next_height = highest_nodes.get(q,(0,0))
            result.append(root_height - deleted_height + next_height)
        return result

# @lc code=end

null = None
print(Solution().treeQueries(TreeBuilder.build([1,3,4,2,null,6,5,null,null,null,null,null,7]),[4]))

#
# @lcpr case=start
# [1,3,4,2,null,6,5,null,null,null,null,null,7]\n[4]\n
# @lcpr case=end

# @lcpr case=start
# [5,8,9,2,1,3,7,4,6]\n[3,2,4,8]\n
# @lcpr case=end

#

