#
# @lc app=leetcode id=590 lang=python3
# @lcpr version=
#
# [590] N-ary Tree Postorder Traversal
#


# @lcpr-template-start

# @lcpr-template-end

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
# @lc code=start
from typing import List

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        return sum((self.postorder(child) for child in root.children), start=[]) + [root.val]
            
# @lc code=end



#
# @lcpr case=start
# [1,null,3,2,4,null,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]\n
# @lcpr case=end

#

