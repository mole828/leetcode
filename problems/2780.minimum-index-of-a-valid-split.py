#
# @lc app=leetcode id=2780 lang=python3
#
# [2780] Minimum Index of a Valid Split
#

# @lc code=start
from collections import Counter
import heapq
from typing import List

from sortedcontainers import SortedList


class Solution:
    # Time Limit Exceeded, 912/917 cases passed
    def minimumIndex(self, nums: List[int]) -> int:
        left = Counter() 
        right = Counter(nums)
        def most(counter: Counter) -> tuple[bool, int]:
            total = counter.total() 
            item, count = counter.most_common(1)[0]
            if count > total//2:
                return True, item
            return False, -1
        for i in range(len(nums)):
            x = nums[i]
            right[x] -= 1
            left[x] += 1
            most_left, left_item = most(left)
            most_right, right_item = most(right)
            if most_left and most_right and left_item == right_item:
                return i
        return -1
    
    class Struct:
        def __init__(self, nums: List[int]):
            self.counter = Counter(nums)
            self.sorted_list = SortedList([(c,v) for v,c in self.counter.items()])
            self.size = len(nums)
        def most(self) -> tuple[bool, int]:
            total = self.size
            count, item = self.sorted_list[-1]
            if count > total//2:
                return True, item
            return False, -1
        def change(self, item: int, d: int) -> None: 
            self.size += d
            last = self.counter[item] 
            self.counter[item] += d
            if last != 0:
                self.sorted_list.remove((last, item))
            self.sorted_list.add((last+d, item))


    def minimumIndex(self, nums: List[int]) -> int:
        left = self.Struct([])
        right = self.Struct(nums)
        for i in range(len(nums)):
            x = nums[i]
            right.change(x, -1)
            left.change(x, 1)
            most_left, left_item = left.most()
            most_right, right_item = right.most()
            if most_left and most_right and left_item == right_item:
                return i
        return -1


# @lc code=end

print(Solution().minimumIndex([1,2,2,2]))
print(Solution().minimumIndex(nums = [2,1,3,1,1,1,7,1,2,1]))