#
# @lc app=leetcode id=3439 lang=python3
#
# [3439] Reschedule Meetings for Maximum Free Time I
#

# @lc code=start

from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        last_end = 0
        free_times = []
        for start, end in sorted(zip(startTime, endTime)):
            if start >= last_end:
                free_times.append(start - last_end)
            last_end = end
        free_times.append(eventTime - last_end)

        max_window = 0
        # for window_left in range(len(free_times)):
        #     window_right = window_left + k
        #     if window_right >= len(free_times):
        #         break
        #     window = free_times[window_left:window_right+1]
        #     max_window = max(max_window, sum(window))
        # return max_window

        window_sum = 0
        window_left = 0
        window_right = 0
        while window_right <= k:
            right_value = free_times[window_right]
            window_sum += right_value
            window_right += 1

        max_window = window_sum

        while window_right < len(free_times):
            window_sum += free_times[window_right]
            window_sum -= free_times[window_left]
            window_left += 1
            window_right += 1
            max_window = max(max_window, window_sum)

        return max_window



# @lc code=end

print(Solution().maxFreeTime(eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]))
print(Solution().maxFreeTime(eventTime=10, k=1, startTime=[0,2,9], endTime=[1,4,10]))
print(Solution().maxFreeTime(eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]))
print(Solution().maxFreeTime(eventTime = 21, k = 2, startTime = [18,20], endTime = [20,21]))