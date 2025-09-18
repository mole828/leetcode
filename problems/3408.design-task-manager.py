#
# @lc app=leetcode id=3408 lang=python3
#
# [3408] Design Task Manager
#

# @lc code=start
import heapq
from typing import List


class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.mp = {}
        self.h = []  
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.mp[taskId] = (priority, userId)
        heapq.heappush(self.h, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.add(self.mp[taskId][1], taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        self.mp[taskId] = (-1, -1)

    def execTop(self) -> int:
        while self.h:
            priority, taskId, userId = heapq.heappop(self.h)
            if self.mp[-taskId] == (-priority, userId):
                self.rmv(-taskId)
                return userId
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
# @lc code=end

# taskManager = TaskManager(
#     [
#         [1, 101, 8],
#         [2, 102, 20],
#         [3, 103, 5],
#     ]
# )
# taskManager.add(4,104,5)
# taskManager.edit(102,9)
# print(taskManager.execTop())
# taskManager.rmv(101)
# taskManager.add(50, 101, 8)
# print(taskManager.execTop())
