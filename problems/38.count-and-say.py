#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        arr = []
        count = 0
        char = s[0]
        for i in range(len(s)):
            if s[i] == char:
                count += 1
            else:
                arr.append(str(count) + char)
                count = 1
                char = s[i]
        arr.append(str(count) + char)
        return "".join(arr)
        
# @lc code=end

print(Solution().countAndSay(4))