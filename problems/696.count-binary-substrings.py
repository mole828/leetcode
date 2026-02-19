#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        arr = []
        count = 0
        last_char = ''
        for char in s:
            if char == last_char:
                count += 1
            else:
                arr.append(count)
                count = 1
                last_char = char
        arr.append(count)
        print(arr)
        ans = 0
        for i in range(1, len(arr)):
            part_a, part_b = arr[i-1], arr[i]
            ans += min(part_a, part_b)
        return ans

# @lc code=end

if __name__ == '__main__':
    print(Solution().countBinarySubstrings("00110011"))