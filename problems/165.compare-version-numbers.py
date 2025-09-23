#
# @lc app=leetcode id=165 lang=python3
# @lcpr version=
#
# [165] Compare Version Numbers
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 2025-09-23 day2
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        iter1 = [int(s) for s in version1.split('.')]
        iter2 = [int(s) for s in version2.split('.')]
        while iter1 or iter2:
            if not iter1:
                iter1.append(0)
            if not iter2:
                iter2.append(0)
            v1, v2 = iter1.pop(0), iter2.pop(0)
            if v1 == v2:
                continue
            return 1 if v1 > v2 else -1
        return 0
# @lc code=end

print(Solution().compareVersion("1.01","1.001"))

#
# @lcpr case=start
# "1.01"\n"1.001"\n
# @lcpr case=end

# @lcpr case=start
# "1.0"\n"1.0.0"\n
# @lcpr case=end

# @lcpr case=start
# "0.1"\n"1.1"\n
# @lcpr case=end

#

