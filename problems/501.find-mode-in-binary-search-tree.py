#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict
from typing import List, Optional


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(lambda:0)
        def count(node: Optional[TreeNode]):
            if node:
                counter[node.val] += 1
                count(node.left)
                count(node.right)
        count(root)
        cm:defaultdict[int,list[int]] = defaultdict(lambda:[])
        for key,value in counter.items():
            cm[value].append(key)
        return cm[max(cm.keys())]
        
# @lc code=end

