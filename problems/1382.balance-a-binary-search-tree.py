#
# @lc app=leetcode id=1382 lang=python3
# @lcpr version=
#
# [1382] Balance a Binary Search Tree
#

from tools.TreeNode import TreeNode

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def to_list(node: TreeNode):
            if not node:
                return []
            return to_list(node.left)+[node.val]+to_list(node.right)
        arr = sorted(to_list(root))
        def to_balance(nums: list[int])->TreeNode:
            if nums:
                i = len(nums)//2
                num = nums[i]
                left = nums[:i]
                right = nums[i+1:]
                return TreeNode(
                    val=num, 
                    left=to_balance(left),
                    right=to_balance(right)
                )
            return None
        return to_balance(arr)
        
# @lc code=end

from tools.TreeNode import TreeBuilder
null = None
print(Solution().balanceBST(TreeBuilder.build(
    [1,null,2,null,3,null,4,null,null]
)))

#
# @lcpr case=start
# [1,null,2,null,3,null,4,null,null]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

#

