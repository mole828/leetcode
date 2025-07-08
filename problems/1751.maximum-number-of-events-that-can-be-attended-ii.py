#
# @lc app=leetcode id=1751 lang=python3
#
# [1751] Maximum Number of Events That Can Be Attended II
#

# @lc code=start
from bisect import bisect_left
import heapq
from typing import List


# 手写 max 更快

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda e: e[1])  # 按照结束时间排序
        max_end = events[-1][1] + 1
        dp = [[0]*k for _ in range(max_end)]
        for day in range(len(dp)):
            if day == 0:
                continue
            else:
                dp[day] = dp[day-1][:]
            while events and events[0][1] == day:
                start, end, val = events.pop(0)
                for i in range(k):
                    dp[day][i] = max(dp[day][i], dp[start][i-1] + val if i > 0 else val)
        print(dp)
        return max(dp[-1])

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda e: e[1])  # 按照结束时间排序
        n = len(events)
        f = [[0] * (k + 1) for _ in range(n + 1)]
        for i, (start_day, _, value) in enumerate(events):
            p = bisect_left(events, start_day, hi=i, key=lambda e: e[1])  # hi=i 表示二分上界为 i（默认为 n）
            for j in range(1, k + 1):
                # 为什么是 p 不是 p+1：上面算的是 >= start_day，-1 后得到 < start_day，但由于还要 +1，抵消了
                f[i + 1][j] = max(f[i][j], f[p][j - 1] + value)
        return f[n][k]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended-ii/solutions/1913087/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-fuip/

# @lc code=end

print(Solution().maxValue(events=[[1,2,4],[3,4,3],[2,3,1]], k=2))
print(Solution().maxValue(events=[[1,2,4],[3,4,3],[2,3,10]], k=2))