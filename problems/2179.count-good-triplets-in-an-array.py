#
# @lc app=leetcode id=2179 lang=python3
#
# [2179] Count Good Triplets in an Array
#

# @lc code=start
from typing import List

from sortedcontainers import SortedList

# Time Limit Exceeded, 78/148 cases passed
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        map1, map2 = {}, {}
        for i in range(n):
            map1[nums1[i]] = i
            map2[nums2[i]] = i
        def is_good(x: int, y: int, z: int, map: dict[int, int]) -> bool:
            if map[x] < map[y] < map[z]:
                return True
            return False
        total = 0
        for x in range(n):
            for y in range(n):
                if x == y:
                    continue
                for z in range(n):
                    if z == x or z == y:
                        continue
                    if is_good(x, y, z, map1):
                        if is_good(x, y, z, map2):
                            total += 1
        return total

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        p = [0] * n
        for i, x in enumerate(nums1):
            p[x] = i

        ans = 0
        sl = SortedList()
        for i, y in enumerate(nums2):
            y = p[y]
            less = sl.bisect_left(y)  # sl 的 [0,less-1] 中的数都是小于 y 的，这有 less 个
            ans += less * (n - 1 - y - (i - less))
            sl.add(y)
        return ans

# @lc code=end

print(Solution().goodTriplets(nums1=[2,0,1,3], nums2=[0,1,2,3]))