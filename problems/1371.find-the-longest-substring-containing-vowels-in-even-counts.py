#
# @lc app=leetcode id=1371 lang=python3
# @lcpr version=
#
# [1371] Find the Longest Substring Containing Vowels in Even Counts
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        offset_map = ['a','e','i','o','u']
        mp = {0:-1}
        curr = 0
        longest = 0
        for i,c in enumerate(s):
            if c in offset_map:
                curr ^= 1 << offset_map.index(c)
            if curr not in mp:
                mp[curr] = i
            else:
                longest = max(longest, i - mp[curr])
            # print(i,c,curr,mp)
        return longest
# @lc code=end

print(Solution().findTheLongestSubstring("eleetminicoworoep"))
print(Solution().findTheLongestSubstring("leetcodeisgreat"))

#
# @lcpr case=start
# "eleetminicoworoep"\n
# @lcpr case=end

# @lcpr case=start
# "leetcodeisgreat"\n
# @lcpr case=end

# @lcpr case=start
# "bcbcbc"\n
# @lcpr case=end

#

