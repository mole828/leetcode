from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 中位数的本质就是比它小的跟比他大的一样或差一个！
        mid = nums.index(k) #找到k的位置
        hash_right = defaultdict(int) # 记录差值：比 k 大的数的个数 - 比 k 小的数的个数
        hash_right[0] = 1 # 中位数本身可以算作一个

        # 从 k 的位置向右遍历
        cnt = 0
        for i in range(mid+1,len(nums)):
            cnt += 1 if nums[i] > k else -1
            hash_right[cnt] += 1
        
        # 从 k 的位置向左遍历
        ans = 0   # 遍历hash_right,k右边的差比k左边的差值和为0，或1 就满足
        cnt = 0
        for i in range(mid,-1,-1):
            if nums[i] > k: cnt += 1
            elif nums[i] < k: cnt -= 1
            ans += hash_right[-cnt] + hash_right[1-cnt]
        return ans