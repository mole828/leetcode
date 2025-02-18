#
# @lc app=leetcode id=2375 lang=python3
#
# [2375] Construct Smallest Number From DI String
#

# @lc code=start
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern) + 1
        bool_pattern = [True if c == 'I' else False for c in pattern]
        num_set = set([1,2,3,4,5,6,7,8,9])
        # res = []
        min_result = float('inf')
        def dfs(i: int, arr: list[int]):
            last = arr[-1]
            if i == n:
                new_result = int(''.join(map(str, arr)))
                nonlocal min_result
                min_result = min(min_result, new_result)
                return
            inc_need = bool_pattern[i-1]
            for num in sorted(num_set - set(arr)):
                inc_real = num > last
                if inc_real == inc_need:
                    dfs(i+1, arr + [num])
        for num in num_set:
            dfs(1, [num])
        return str(min_result)
            

# @lc code=end

print(Solution().smallestNumber('IIIDIDDD'))