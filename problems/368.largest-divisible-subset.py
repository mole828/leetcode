#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
from typing import List

# Memory Limit Exceeded, 47 / 49 testcases passed
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        root = {}

        def buildTree(node: dict, num: int):
            # print(F"dfs({node},{num})")
            node[num] = {}
            for key in node:
                if key == num:
                    continue
                if key%num==0 or num%key==0:
                    buildTree(node[key], num)

        for num in nums:
            buildTree(root, num)

        def findDeep(node: dict) -> list:
            longest = []
            if len(node)==0:
                return longest
            for num in node:
                arr = [num] + findDeep(node[num])
                if len(arr)>len(longest):
                    longest = arr 
            return longest
                
        print(root)

        return findDeep(root)
                
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        max_size, max_index = 1, 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i

        result = []
        num = nums[max_index]
        for i in range(max_index, -1, -1):
            if num % nums[i] == 0 and dp[i] == max_size:
                result.append(nums[i])
                num = nums[i]
                max_size -= 1

        return result


# @lc code=end

print(Solution().largestDivisibleSubset([1,2,3]))