#
# @lc app=leetcode id=995 lang=python3
# @lcpr version=
#
# [995] Minimum Number of K Consecutive Bit Flips
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        has: dict[int, int] = {}
        def hash(nums: List[int]) -> int:
            return int('0b'+''.join(str(i) for i in nums), base=2)
        def dfs(nums: List[int]) -> int:
            # print(f"dfs({nums})")
            _hash = hash(nums)
            if all(nums):
                return 0
            if _hash in has:
                return has[_hash]
            has[_hash] = float('inf')
            son = [float('inf')]
            for i in range(len(nums)-k+1):
                new_nums = nums.copy()
                for j in range(i,i+k):
                    new_nums[j] = 1 - new_nums[j]
                son.append(dfs(new_nums))
            has[_hash] = min(son) + 1
            return has[_hash]
        step = dfs(nums)
        return -1 if step == float('inf') else step
    
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flipped = 0
        res = 0
        isFlipped = [0] * n
        
        for i in range(n):
            if i >= k:
                flipped ^= isFlipped[i - k]
            if flipped == nums[i]:
                if i + k > n:
                    return -1
                isFlipped[i] = 1
                flipped ^= 1
                res += 1
        
        return res
    
# @lc code=end

print(Solution().minKBitFlips([0,1,0], 1))
print(Solution().minKBitFlips([0,0,0,1,0,1,1,0], 3))

#
# @lcpr case=start
# [0,1,0]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,1,0]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,1,0,1,1,0]\n3\n
# @lcpr case=end

#

