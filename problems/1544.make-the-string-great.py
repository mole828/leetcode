#
# @lc app=leetcode id=1544 lang=python3
# @lcpr version=
#
# [1544] Make The String Great
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str: 
        good = s 
        def make() -> bool: 
            nonlocal good
            has_remove = False
            i = 1 
            while i<len(good):
                if all([
                    good[i].lower() == good[i-1].lower(), 
                    good[i] != good[i-1], 
                ]):
                    good = good[:i-1] + good[i+1:] 
                    i -= 1 
                    has_remove = True
                i += 1 
            return has_remove
        while make():
            pass
        return good 
# @lc code=end

print(Solution().makeGood('abBAcC'))

#
# @lcpr case=start
# "leEeetcode"\n
# @lcpr case=end

# @lcpr case=start
# "abBAcC"\n
# @lcpr case=end

# @lcpr case=start
# "s"\n
# @lcpr case=end

#

