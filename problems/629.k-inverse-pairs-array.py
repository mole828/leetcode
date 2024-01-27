#
# @lc app=leetcode id=629 lang=python3
#
# [629] K Inverse Pairs Array
#

# @lc code=start
from functools import cache

# Time Limit Exceeded
class Solution:
    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        print(f"kInversePairs({n},{k})")
        if k <= 0:
            return 1
        if k == 1:
            return n-1 
        if n == 1:
            return 0
        return sum(
            self.kInversePairs(n-1,j) - (self.kInversePairs(n-1,j-n) if j>=n else 0)
            for j in range(k+1)
        )
    
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        M = 1000000007
        if k == 0:
            return 1
        if n == 1:
            return 1 if k == 0 else 0

        current_count = [0] * (k + 1)
        current_count[0] = 1
        previous_count = [0] * (k + 1)

        for i in range(n - 2, -1, -1):
            total_count = 0
            threshold = n - i

            for j in range(0, k + 1):
                total_count += current_count[j]

                if j >= threshold:
                    total_count -= current_count[j - threshold]

                total_count %= M
                previous_count[j] = total_count

            current_count, previous_count = previous_count, current_count

        return current_count[k]
        #Upvote me if it helps
        
# @lc code=end

[1,2,3,4]
[1,4,2,3]
def countInverse(nums: list[int]) -> int:
    length = len(nums)
    count = 0
    for i in range(length):
        vi = nums[i]
        for j in range(i+1, length):
            vj = nums[j]
            if vj < vi :
                count += 1
    return count

# print(countInverse([2,1,4,3]))

print(Solution().kInversePairs(3,3))
print(Solution().kInversePairs(3,2))
