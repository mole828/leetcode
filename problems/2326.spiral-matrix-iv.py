#
# @lc app=leetcode id=2326 lang=python3
# @lcpr version=
#
# [2326] Spiral Matrix IV
#

from tools.ListNode import ListNode

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1 for i in range(n)] for j in range(m)]
        i = complex(0, 1)
        direction = complex(0,1) 
        place = complex(0,0)
        while head:
            ans[int(place.real)][int(place.imag)] = head.val
            head = head.next
            place += direction
            if not (0 <= place.real < m and 0 <= place.imag < n and ans[int(place.real)][int(place.imag)] == -1):
                place -= direction
                direction *= -i
                place += direction
        
        return ans
# @lc code=end

print(Solution().spiralMatrix(3,5,ListNode.build([3,0,2,6,8,1,7,9,4,2,5,5,0])))

#
# @lcpr case=start
# 3\n5\n[3,0,2,6,8,1,7,9,4,2,5,5,0]\n
# @lcpr case=end

# @lcpr case=start
# 1\n4\n[0,1,2]\n
# @lcpr case=end

#

