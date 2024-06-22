#
# @lc app=leetcode id=1248 lang=python3
# @lcpr version=
#
# [1248] Count Number of Nice Subarrays
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        subs =( 
            nums[left:right+1] for left in range(len(nums)) for right in range(left, len(nums))
        )
        nice_subs = [
            sub for sub in subs if sum(x%2 for x in sub)==k
        ]
        print(nice_subs)
        return len(nice_subs)
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        index = [0]
        for num in nums:
            index.append(index[-1]+num%2)
        count = Counter(index)
        print(index)
        total = 0
        for x in index:
            total += count[x+k]
        return total
        
# @lc code=end

print(Solution().numberOfSubarrays([1,1,2,1,1,],3))

#
# @lcpr case=start
# [1,1,2,1,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6]\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,1,2,2,1,2,2,2]\n2\n
# @lcpr case=end

#

