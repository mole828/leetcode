from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(r)
        ans = [False] * n

        for i in range(n):
            t = sorted(nums[l[i]:r[i] + 1])
            d = t[1] - t[0]
            flag = True
            for j in range(1, len(t)):
                if t[j] - t[j -1] != d:
                    flag = False
                    break
            ans[i] = flag
        return ans