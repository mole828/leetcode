#
# @lc app=leetcode id=1381 lang=python3
# @lcpr version=
#
# [1381] Design a Stack With Increment Operation
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = [0] * maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if self.top != len(self.stk) - 1:
            self.top += 1
            self.stk[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return -1
        self.top -= 1
        return self.stk[self.top + 1]

    def increment(self, k: int, val: int) -> None:
        lim = min(k, self.top + 1)
        for i in range(lim):
            self.stk[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end



