#
# @lc app=leetcode id=2096 lang=python3
# @lcpr version=
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
#

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
from typing import Optional


class Solution:
    # Time Limit Exceeded, 328/332 cases passed (N/A)
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(node: Optional[TreeNode], target: int) -> list[str]:
            if node:
                if node.val == target:
                    return ["_"]
                left = find(node.left, target)
                if left:
                    return ["L"]+left
                right = find(node.right, target)
                if right:
                    return ["R"]+right
            return None
        start_path = find(root, startValue)
        dest_path = find(root, destValue)
        while start_path and dest_path and start_path[0]==dest_path[0]:
            start_path.pop(0)
            dest_path.pop(0)

        start_path.pop()
        dest_path.pop()
        print(start_path, dest_path)
        
        return "U"*len(start_path)+''.join(dest_path)
    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(n: TreeNode, val: int, path: list[str]) -> bool:
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path += "L"
            elif n.right and find(n.right, val, path):
                path += "R"
            return path
        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))
        
# @lc code=end

null = None
print(Solution().getDirections(TreeBuilder.build([5,1,2,3,null,6,4]),3,6))

#
# @lcpr case=start
# [5,1,2,3,null,6,4]\n3\n6\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n1\n
# @lcpr case=end

#

