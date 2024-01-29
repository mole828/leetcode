#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:
    _data: list[int]
    def __init__(self):
        self._data = []

    def push(self, x: int) -> None:
        self._data.append(x)

    def pop(self) -> int:
        return self._data.pop(0)

    def peek(self) -> int:
        return self._data[0]

    def empty(self) -> bool:
        return len(self._data)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

