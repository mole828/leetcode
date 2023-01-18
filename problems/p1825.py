
from bisect import bisect_left
from collections import deque


class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.queue = deque()
        self.sorted = []
        self.size = m - 2 * k
        self.s = 0

    def addElement(self, num: int) -> None:
        self.queue.append(num)
        if len(self.queue) == self.m:
            self.sorted = sorted(self.queue)
            self.s = sum(self.sorted[self.k:-self.k])
        if len(self.queue) > self.m:
            i = bisect_left(self.sorted, self.queue.popleft())
            if i < self.k:
                self.s -= self.sorted[self.k]
            elif i >= len(self.sorted) - self.k:
                self.s -= self.sorted[-self.k-1]
            else:
                self.s -= self.sorted[i]
            self.sorted.pop(i)
            j = bisect_left(self.sorted, num)
            if j < self.k:
                self.s += self.sorted[self.k-1]
            elif j > len(self.sorted)-self.k:
                self.s += self.sorted[-self.k]
            else:
                self.s += num
            self.sorted.insert(j, num)
        # print(self.queue, self.sorted, self.s)

    def calculateMKAverage(self) -> int:
        if len(self.queue) < self.m:
            return -1
        return int(self.s / self.size)



# Your MKAverage object will be instantiated and called as such:
obj = MKAverage(3, 1)
obj.addElement(3)
obj.addElement(1)
obj.calculateMKAverage()
obj.addElement(10)
obj.calculateMKAverage()
obj.addElement(5)
obj.addElement(5)
obj.addElement(5)
obj.calculateMKAverage()
