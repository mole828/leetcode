#
# @lc app=leetcode id=432 lang=python3
# @lcpr version=
#
# [432] All O`one Data Structure
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
import heapq


class AllOne:

    def __init__(self):
        self.counter = Counter()
        self.min_heap = []
        self.max_heap = []

    def inc(self, key: str) -> None:
        self.counter[key] += 1
        heapq.heappush(self.min_heap, (self.counter[key], key))
        heapq.heappush(self.max_heap, (-self.counter[key], key))

    def dec(self, key: str) -> None:
        self.counter[key] -= 1
        if self.counter[key] == 0:
            del self.counter[key]

    def getMaxKey(self) -> str:
        while self.max_heap:
            count, key = self.max_heap[0]
            if self.counter[key] == -count:
                return key
            heapq.heappop(self.max_heap)
        return ''

    def getMinKey(self) -> str:
        while self.min_heap:
            count, key = self.min_heap[0]
            if self.counter[key] == count:
                return key
            heapq.heappop(self.min_heap)
        return ''
        

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end



