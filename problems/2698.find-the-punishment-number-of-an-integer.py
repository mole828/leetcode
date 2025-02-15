#
# @lc app=leetcode id=2698 lang=python3
# @lcpr version=30204
#
# [2698] Find the Punishment Number of an Integer
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

from functools import cache


def dfs_check(num: int):
    pow_num = str(num**2)
    n=len(pow_num)
    @cache
    def dfs(i,sums,is_num):
        if sums+is_num>num:
            return False
        if i==n:
            if sums+is_num==num:
                return True
            return False
        if dfs(i+1,sums+is_num,int(pow_num[i])) or dfs(i+1,sums,is_num*10+int(pow_num[i])):
            return True
        return False
    return dfs(0,0,0)

def findBefore(num: int):
    ans = []
    for i in range(1, num+1):
        if dfs_check(i):
            ans.append(i)
    return ans
# print(findBefore(1000))
nums = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
import bisect
class Solution:
    def punishmentNumber(self, n: int) -> int:
        return sum([n**2 for n in nums[:bisect.bisect_right(nums, n)]])
# @lc code=end

print(Solution().punishmentNumber(10))

#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 37\n
# @lcpr case=end

#

