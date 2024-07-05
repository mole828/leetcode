#
# @lc app=leetcode id=2058 lang=python3
# @lcpr version=
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
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
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_index = []
        ib = 1
        a,b,c = head, head.next, head.next.next
        while a and b and c:
            if a.val>b.val<c.val or a.val<b.val>c.val:
                critical_index.append(ib)
            a,b,c = b,c,c.next
            ib += 1
        if len(critical_index) < 2:
            return [-1,-1]
        print(critical_index)
        return [min(critical_index[i]-critical_index[i-1] for i in range(1, len(critical_index))), critical_index[-1]-critical_index[0]]
        
        
# @lc code=end



#
# @lcpr case=start
# [3,1]\n
# @lcpr case=end

# @lcpr case=start
# [5,3,1,2,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2,2,3,2,2,2,7]\n
# @lcpr case=end

#

