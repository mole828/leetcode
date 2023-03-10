from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        t = sum(nums) % p
        if t == 0:
            return 0
        pre,cur,n = {0:-1},0,len(nums)
        ans = n
        for i in range(n):
            cur += nums[i]
            cur %= p
            need = (cur - t + p) % p
            if need in pre:
                ans = min(ans,i - pre[need])
            pre[cur] = i
        return ans if ans != n else -1     