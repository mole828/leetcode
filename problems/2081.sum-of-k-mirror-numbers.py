#
# @lc app=leetcode id=2081 lang=python3
#
# [2081] Sum of k-Mirror Numbers
#

# @lc code=start

table = []
for i in range(1, 12):
    for j in range(10 ** ((i - 1) // 2), 10 ** ((i + 1) // 2)):
        if i % 2: table.append(int(str(j) + str(j)[-2::-1]))
        else: table.append(int(str(j) + str(j)[::-1]))

d = {}

# 将十进制数转化为k进制
def chBase(num, k):
    if num < k:
        return str(num)
    return str(chBase(num // k, k)) + str(num % k)


def mirror(k, n):
    ans = []
    i = 0
    while len(ans) < n:
        s = chBase(table[i], k)
        if s == s[::-1]:
            ans.append(table[i])
        i += 1

    return ans


for i in range(2, 10):
    d[i] = mirror(i, 30)

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        return sum(d[k][:n])
# @lc code=end

print(Solution().kMirror(4,30))