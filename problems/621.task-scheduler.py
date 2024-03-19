#
# @lc app=leetcode id=621 lang=python3
# @lcpr version=
#
# [621] Task Scheduler
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0 
        count = Counter(tasks)
        last_time = {k:-float('inf') for k in count}
        while count.total():
            for task,_ in count.most_common():
                # print({'time':time, 'last_time':last_time[task]})
                if count[task] and time-last_time[task]>n:
                    # print(f"time:{time}, do:{task}")
                    count[task] -= 1 
                    last_time[task] = time
                    break

            time += 1
            # print(time, count, last_time)
        return time
# @lc code=end



print(Solution().leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))


#
# @lcpr case=start
# ["A","A","A","B","B","B"]\n2\n
# @lcpr case=end

# @lcpr case=start
# ["A","C","A","B","D","B"]\n1\n
# @lcpr case=end

# @lcpr case=start
# ["A","A","A", "B","B","B"]\n3\n
# @lcpr case=end

#

