#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
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

# day1 Feb 09, 2024
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

# day2 May 06, 2025
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        @cache
        def findDeep(index: int) -> List[int]:
            this_num = nums[index]
            longest = []
            for j in range(index):
                if this_num % nums[j] == 0:
                    arr = findDeep(j)
                    if len(arr) > len(longest):
                        longest = arr
            return [this_num] + longest
        longest = []
        for i in range(len(nums)):
            arr = findDeep(i)
            if len(arr) > len(longest):
                longest = arr
        return longest

# @lc code=end


print(Solution().largestDivisibleSubset([1,2,3]))