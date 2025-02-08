#
# @lc app=leetcode id=2349 lang=python3
# @lcpr version=30204
#
# [2349] Design a Number Container System
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict

from sortedcontainers import SortedList


class NumberContainers:

    def __init__(self):
        self.data = defaultdict(SortedList)
        self.map = defaultdict(None)

    def change(self, index: int, number: int) -> None:
        if self.map.get(index, None):
            self.data[self.map[index]].remove(index)
        self.map[index] = number
        self.data[number].add(index)

    def find(self, number: int) -> int:
        if not self.data[number]:
            return -1
        return self.data[number][0]
        

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
# @lc code=end



