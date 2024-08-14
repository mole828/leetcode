#
# @lc app=leetcode id=719 lang=python3
# @lcpr version=
#
# [719] Find K-th Smallest Pair Distance
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from bisect import bisect_left
from collections import Counter
from typing import List

from sortedcontainers import SortedList

# Time Limit Exceeded, 16/19 cases passed (N/A)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        l: List[int] = SortedList()
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i+1, len(nums)):
                b = nums[j]
                diff = abs(a-b)
                l.add(diff)
        print(l)
        return l[k-1]

# Time Limit Exceeded, 18/19 cases passed (N/A)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        result_list = Counter()
        for a in counter:
            for b in counter:
                diff = abs(a-b)
                result_list[diff] += counter[a] * counter[b]
                if a==b:
                    result_list[0] -= counter[a]
        c = sorted(result_list.items())
        # print(c)
        kk = 2*k
        for diff, count in c:
            if count >= kk:
                return diff
            kk -= count

# 链接：https://leetcode.cn/problems/find-k-th-smallest-pair-distance/solutions/1600107/zhao-chu-di-k-xiao-de-shu-dui-ju-chi-by-xwfgf/
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(mid: int) -> int:
            cnt = 0
            for j, num in enumerate(nums):
                i = bisect_left(nums, num - mid, 0, j)
                cnt += j - i
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key=count)
      

            
# @lc code=end

print(Solution().smallestDistancePair([1,3,1], 1)) # 0
print(Solution().smallestDistancePair([1,6,1], 3)) # 0
print(Solution().smallestDistancePair([62,100,4], 2)) # 0

#
# @lcpr case=start
# [1,3,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,6,1]\n3\n
# @lcpr case=end

#

