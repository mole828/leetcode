#
# @lc app=leetcode id=1405 lang=python3
# @lcpr version=
#
# [1405] Longest Happy String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            cnt.sort(key=lambda x: -x[0])
            hasNext = False
            for i, (c, ch) in enumerate(cnt):
                if c <= 0:
                    break
                if len(ans) >= 2 and ans[-2] == ch and ans[-1] == ch:
                    continue
                hasNext = True
                ans.append(ch)
                cnt[i][0] -= 1
                break
            if not hasNext:
                return ''.join(ans)
            
# @lc code=end

print(Solution().longestDiverseString(1, 1, 7))

#
# @lcpr case=start
# 1\n1\n7\n
# @lcpr case=end

# @lcpr case=start
# 7\n1\n0\n
# @lcpr case=end

#

