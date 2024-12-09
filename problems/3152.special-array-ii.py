#
# @lc app=leetcode id=3152 lang=python3
# @lcpr version=
#
# [3152] Special Array II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import bisect
from typing import List

# Time Limit Exceeded, 535/536 cases passed (N/A)
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ns = [num%2 for num in nums]
        diff = [ns[i]!=ns[i+1] for i in range(len(ns)-1)]
        print(diff)
        return [all(diff[a:b]) for a,b in queries]
    
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ns = [num%2 for num in nums]
        diff = [i for i in range(len(ns)-1) if ns[i]==ns[i+1]]
        print(diff)
        def binary_search(a,b):
            left = bisect.bisect_left(diff, a)
            right = bisect.bisect_left(diff, b)
            return right-left==0
        return [binary_search(a,b) for a,b in queries]
        
# @lc code=end



#
# @lcpr case=start
# [3,4,1,2,6]\n[[0,4]]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,1,6]\n[[0,2],[2,3]]\n
# @lcpr case=end

#

