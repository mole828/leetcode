from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def judge(k: int) -> bool:
            temp = maxOperations
            for i in nums:
                if temp < 0: return False
                if i > k: temp -= (i + k - 1) // k - 1
            return temp >= 0
        l, r = 1, max(nums)
        while l <= r:
            m = (l + r) // 2
            if judge(m): r = m - 1
            else: l = m + 1
        return r + 1