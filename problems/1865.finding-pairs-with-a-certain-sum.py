#
# @lc app=leetcode id=1865 lang=python3
# @lcpr version=30204
#
# [1865] Finding Pairs With a Certain Sum
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List


class FindSumPairs:
    nums1: List[int]
    nums2: List[int]
    nums1_dict: dict[int, set[int]]
    nums2_dict: dict[int, set[int]]
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums1_dict = defaultdict(set)
        for i,v in enumerate(nums1):
            self.nums1_dict[v].add(i)
        self.nums2 = nums2
        self.nums2_dict = defaultdict(set)
        for i,v in enumerate(nums2):
            self.nums2_dict[v].add(i)

    def add(self, index: int, val: int) -> None:
        oldValue = self.nums2[index]
        newValue = oldValue + val
        self.nums2[index] = newValue
        self.nums2_dict[oldValue].remove(index)
        if len(self.nums2_dict[oldValue]) == 0:
            del self.nums2_dict[oldValue]
        self.nums2_dict[newValue].add(index)

    def count(self, tot: int) -> int:
        return sum((len(v2)*len(self.nums2_dict[tot-k2])) for k2,v2 in self.nums1_dict.items())


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
# @lc code=end



