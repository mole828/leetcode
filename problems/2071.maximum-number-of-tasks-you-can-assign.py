#
# @lc app=leetcode id=2071 lang=python3
# @lcpr version=30204
#
# [2071] Maximum Number of Tasks You Can Assign
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque
from functools import cache
import heapq
from typing import List


class Solution:
    # Wrong Answer, 29/49 cases passed
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        heapq.heapify(tasks)
        heapq.heapify(workers)
        cnt = 0
        while tasks and workers:
            task = heapq.heappop(tasks) 
            worker = heapq.heappop(workers)
            if task <= worker:
                cnt += 1
                continue
            if pills > 0 and task <= strength + worker:
                cnt += 1
                pills -= 1
                continue
            heapq.heappush(tasks, task)
        return cnt
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        @cache
        def dfs(worker_index:int, task_index:int, pills_last:int)->int:
            if task_index == len(tasks):
                return 0
            if worker_index == len(workers):
                return 0
            ans = []
            # do nothing
            ans.append(dfs(worker_index+1, task_index, pills_last))
            # do task
            if workers[worker_index] >= tasks[task_index]:
                ans.append(1 + dfs(worker_index+1, task_index+1, pills_last))
            # do task with pills
            if pills_last > 0 and workers[worker_index] + strength >= tasks[task_index]:
                ans.append(1 + dfs(worker_index+1, task_index+1, pills_last-1))
            return max(ans)
        return dfs(0, 0, pills)
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def check(k: int) -> bool:
            # 贪心：用最强的 k 名工人，完成最简单的 k 个任务
            i, p = 0, pills
            valid_tasks = deque()
            for w in workers[-k:]:  # 枚举工人
                # 在吃药的情况下，把能完成的任务记录到 valid_tasks 中
                while i < k and tasks[i] <= w + strength:
                    valid_tasks.append(tasks[i])
                    i += 1
                # 即使吃药也无法完成任务
                if not valid_tasks:
                    return False
                # 无需吃药就能完成（最简单的）任务
                if w >= valid_tasks[0]:
                    valid_tasks.popleft()
                    continue
                # 必须吃药
                if p == 0:  # 没药了
                    return False
                p -= 1
                # 完成（能完成的）最难的任务
                valid_tasks.pop()
            return True

        left, right = 0, min(len(tasks), len(workers)) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left


# @lc code=end

# print(Solution().maxTaskAssign(tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1))
# print(Solution().maxTaskAssign(tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5))
# print(Solution().maxTaskAssign(tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10))
print(Solution().maxTaskAssign(tasks = [5,9,8,5,9], workers = [1,6,4,2,6], pills = 1, strength = 5))

#
# @lcpr case=start
# [3,2,1]\n[0,3,3]\n1\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,4]\n[0,0,0]\n1\n5\n
# @lcpr case=end

# @lcpr case=start
# [10,15,30]\n[0,10,10,10,10]\n3\n10\n
# @lcpr case=end

#

