#
# @lc app=leetcode id=2981 lang=python3
# @lcpr version=
#
# [2981] Find Longest Special Substring That Occurs Thrice I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        count: dict[str, dict[int, list[int]]] = defaultdict(lambda:defaultdict(lambda:[]))
        last_char = '#'
        seq = 1
        for i, ch in enumerate(s):
            if ch == last_char:
                seq += 1
            else:
                seq = 1
            for j in range(seq):
                count[ch][j].append(i)
            last_char = ch
        print(count)
        ans = -1
        for ch in count:
            for seq, indices in count[ch].items():
                if len(indices) < 3:
                    continue
                ans = max(ans, seq+1)
        return ans
    
# @lc code=end

print(Solution().maximumLength("aaaa"))
print(Solution().maximumLength("abcaba"))

#
# @lcpr case=start
# "aaaa"\n
# @lcpr case=end

# @lcpr case=start
# "abcdef"\n
# @lcpr case=end

# @lcpr case=start
# "abcaba"\n
# @lcpr case=end

#

