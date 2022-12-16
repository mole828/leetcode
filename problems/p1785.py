from typing import List
import math

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return math.ceil(abs(sum(nums)-goal)/limit)