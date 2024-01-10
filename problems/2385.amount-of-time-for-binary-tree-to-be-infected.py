#
# @lc app=leetcode id=2385 lang=python3
#
# [2385] Amount of Time for Binary Tree to Be Infected
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    parent: 'TreeNode'
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # startNode: TreeNode
        thisTime: list[TreeNode] = []
        def dfs(node: Optional[TreeNode]):
            print(f"dfs({node.val})")
            if node.val == start:
                # startNode = node 
                thisTime.append(node)
            if node.left:
                node.left.parent = node 
                dfs(node.left)
            if node.right:
                node.right.parent = node 
                dfs(node.right)
        dfs(root)
        time = 0
        hasPass: set[TreeNode] = set(thisTime)
        while thisTime:
            print([node.val for node in thisTime if node])
            nextTime = [] 
            for fromNode in thisTime:
                if fromNode:
                    for toNode in [fromNode.parent if 'parent' in fromNode.__dict__ else None, fromNode.left, fromNode.right]:
                        if toNode:
                            if toNode in hasPass:
                                continue
                            hasPass.add(toNode)
                            nextTime.append(toNode)
            thisTime = nextTime
            time += 1
        
        return time - 1
# @lc code=end

from tools.TreeNode import TreeBuilder
null = None

root1 = TreeNode(1,
            TreeNode(5, None, TreeNode(4, TreeNode(9), TreeNode(2))),
            TreeNode(3, TreeNode(10), TreeNode(6))
        )
print(Solution().amountOfTime(root1, start=3))

print(Solution().amountOfTime(TreeBuilder.build([1,2,null,3,null,4,null,5]), 3))