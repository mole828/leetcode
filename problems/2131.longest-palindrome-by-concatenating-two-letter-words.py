#
# @lc app=leetcode id=2131 lang=python3
# @lcpr version=30204
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import Counter, List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        ans = x = 0
        for k, v in cnt.items():
            if k[0] == k[1]:
                x += v & 1
                ans += (
                    v // 2 * 2 # 有两个算两个, 有单独的忽略
                ) * 2
            else:
                ans += min(v, cnt[k[::-1]]) * 2
        ans += 2 if x else 0
        return ans


# @lc code=end



#
# @lcpr case=start
# ["lc","cl","gg"]\n
# @lcpr case=end

# @lcpr case=start
# ["ab","ty","yt","lc","cl","ab"]\n
# @lcpr case=end

# @lcpr case=start
# ["cc","ll","xx"]\n
# @lcpr case=end

#

