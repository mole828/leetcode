#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start

class Solution(object):
    def findJudge(self, n, trust):
        trusting = [0] * (n + 1)
        trusted = [0] * (n + 1)

        for t in trust:
            trusting[t[0]] += 1
            trusted[t[1]] += 1

        ans = -1

        for i in range(1, n + 1):
            if trusting[i] == 0 and trusted[i] == n - 1:
                ans = i

        return ans
        
# @lc code=end

print(Solution().findJudge(3,[[1,3],[2,3]]))