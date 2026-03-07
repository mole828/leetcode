#
# @lc app=leetcode id=1888 lang=python3
#
# [1888] Minimum Number of Flips to Make the Binary String Alternating
#

# @lc code=start
class Solution:
    def minFlips(self, s: str) -> int:
        def minOperations(st: str) -> int:
            diff = [0, 0]
            for c in st:
                num = int(c)
                diff[num] += 1
                diff.reverse()
            return min(diff)
        ss = s + s
        min_flip = float("inf")
        for i in range(len(s)):
            min_flip = min(min_flip, minOperations(ss[i: i + len(s)]))
        return min_flip
    
class Solution:
    def minFlips(self, s: str) -> int:
        len_s = len(s)
        ss = s + s
        diff = [0, 0]
        for c in s:
            num = int(c)
            diff[num] += 1
            diff.reverse()
        min_flip = min(diff)
        for c in s:
            num = int(c)
            diff[(len_s + num) % 2] -= 1
            diff[(len_s + num + 1) % 2] += 1
            # why?
            diff.reverse()
            print(diff)
            min_flip = min(min_flip, min(diff))
        return min_flip

class Solution:
    def minFlips(self, s: str) -> int:
        ans = n = len(s)
        cnt = 0
        for i in range(n * 2 - 1):
            if ord(s[i % n]) % 2 != i % 2:
                cnt += 1
            left = i - n + 1
            if left < 0:
                continue
            ans = min(ans, cnt, n - cnt)
            if ord(s[left]) % 2 != left % 2:
                cnt -= 1
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/solutions/815298/cong-qian-wang-hou-pi-pei-cong-hou-wang-uiq6a/

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    # print(s.minFlips("111000"))
    # print(s.minFlips("010"))
    print(s.minFlips("01001001101"))