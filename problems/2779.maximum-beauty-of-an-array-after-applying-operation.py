#
# @lc app=leetcode id=2779 lang=python3
# @lcpr version=
#
# [2779] Maximum Beauty of an Array After Applying Operation
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List

# Time Limit Exceeded, 605 / 621 testcases passed
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        counter = Counter()
        for num in nums:
            for i in range(num - k, num + k + 1):
                counter[i] += 1
        return max(counter.values())
    
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        events = []
        for num in nums:
            events.append((num-k, 1))
            events.append((num+k+1, -1))
        events.sort()
        max_beauty = 0
        current_count = 0
        for _, delta in events:
            current_count += delta
            max_beauty = max(max_beauty, current_count)
        return max_beauty
        
# @lc code=end



#
# @lcpr case=start
# [4,6,1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n10\n
# @lcpr case=end

#

