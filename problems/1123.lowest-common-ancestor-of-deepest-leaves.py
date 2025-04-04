#
# @lc app=leetcode id=1123 lang=python3
# @lcpr version=30204
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#


# @lcpr-template-start

# @lcpr-template-end
from tools.TreeNode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        class Context:
            def __init__(self):
                self.max_depth = -1
                self.max_depth_node = []
        parents = {root: None}
        ctx = Context()
        def dfs(node: TreeNode, depth: int):
            if depth > ctx.max_depth:
                ctx.max_depth = depth
                ctx.max_depth_node = [node]
            elif depth == ctx.max_depth:
                ctx.max_depth_node.append(node)
            if node.left:
                parents[node.left] = node
                dfs(node.left, depth + 1)
            if node.right:
                parents[node.right] = node
                dfs(node.right, depth + 1)
        dfs(root, 0)
        batch = ctx.max_depth_node
        while len(batch) > 1:
            next_batch = set()
            for node in batch:
                next_batch.add(parents[node])
            batch = next_batch
        return batch.pop()

# @lc code=end



#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,3,null,2]\n
# @lcpr case=end

#

