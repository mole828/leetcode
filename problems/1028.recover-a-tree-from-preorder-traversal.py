#
# @lc app=leetcode id=1028 lang=python3
# @lcpr version=30204
#
# [1028] Recover a Tree From Preorder Traversal
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
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        words = traversal.split('-')
        print(words)
        root = TreeNode(val=int(words.pop(0)))
        def insert(node: TreeNode, depth: int, new_node: TreeNode):
            if depth == 0:
                if node.left:
                    node.right = new_node
                else:
                    node.left = new_node
                return
            if node.right: 
                insert(node.right, depth-1, new_node)
                return
            if node.left:
                insert(node.left, depth-1, new_node)
                return
            raise ValueError("No child to insert")
        
        depth = 0
        while words:
            word = words.pop(0)
            if word == '':
                depth += 1
                continue
            new_node = TreeNode(val=int(word))
            insert(root, depth, new_node)
            depth = 0
        return root
            
            
# @lc code=end

print(Solution().recoverFromPreorder("1-2--3--4-5--6--7"))

#
# @lcpr case=start
# "1-2--3--4-5--6--7"\n
# @lcpr case=end

# @lcpr case=start
# "1-2--3---4-5--6---7"\n
# @lcpr case=end

# @lcpr case=start
# "1-401--349---90--88"\n
# @lcpr case=end

#

