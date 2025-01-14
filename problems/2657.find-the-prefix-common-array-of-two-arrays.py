#
# @lc app=leetcode id=2657 lang=python3
# @lcpr version=
#
# [2657] Find the Prefix Common Array of Two Arrays
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB = set()
        ans = []
        for ca, cb in zip(A, B):
            setA.add(ca)
            setB.add(cb)
            ans.append(len(setA & setB))
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,3,2,4]\n[3,1,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,1]\n[3,1,2]\n
# @lcpr case=end

#

