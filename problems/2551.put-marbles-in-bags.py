#
# @lc app=leetcode id=2551 lang=python3
#
# [2551] Put Marbles in Bags
#

# @lc code=start
from typing import List, Optional

log = print
# def log(*args, **kwargs): pass

class Solution:
    class CutStatus:
        data: int
        max_cut_index: int

        @staticmethod
        def range_value(left: int, right: int, weight: List[int]) -> int:
            log('range_value', left, right, weight[left]+weight[right])  
            return weight[left] + weight[right]
        
        def __init__(self, data: int = 0):
            self.cut_times = 0
            self.data = data
            self.max_cut_index = -1
        def cut(self, value: int):
            self.cut_times += 1
            self.data |= 1 << value
            self.max_cut_index = max(self.max_cut_index, value)
            return self
        def result(self, weight: List[int]) -> int:
            left, right = 0, 0
            sum_of_ranges = 0
            d = self.data
            while d:
                while d and d%2 == 0:
                    d >>= 1
                    right += 1
                value = Solution.CutStatus.range_value(left, right, weight)
                sum_of_ranges += value
                left = right = right + 1

                d >>= 1
            sum_of_ranges += Solution.CutStatus.range_value(left, -1, weight)
            return sum_of_ranges
        def copy(self) -> 'Solution.CutStatus':
            new = Solution.CutStatus()
            new.data = self.data
            new.cut_times = self.cut_times
            return new


    def putMarbles(self, weights: List[int], k: int) -> int:
        cut_times = k - 1
        class D:
            max_cut_value = float('-inf')
            max_cut_status = Solution.CutStatus()
            min_cut_value = float('inf')
            min_cut_status = Solution.CutStatus()
        d = D()
        right = len(weights) - 1
        def dfs(status: Solution.CutStatus):
            if status.cut_times == cut_times:
                # log(status.result(weights))
                this_cut_value = status.result(weights)
                if this_cut_value > d.max_cut_value:
                    d.max_cut_status = status
                    d.max_cut_value = this_cut_value
                if this_cut_value < d.min_cut_value:
                    d.min_cut_status = status
                    d.min_cut_value = this_cut_value
                return
            for i in range(status.max_cut_index+1, right):
                dfs(status.copy().cut(i))
        dfs(Solution.CutStatus())
        log(d.max_cut_value, d.min_cut_value)
        return d.max_cut_value - d.min_cut_value
    
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        for i in range(len(weights)-1):
            weights[i] += weights[i+1]
        weights.pop()
        weights.sort()
        # print(weights[-k+1:], weights[:k-1]) 
        return sum(weights[len(weights)-k+1:]) - sum(weights[:k-1])

# @lc code=end

log(Solution().putMarbles(weights = [1,3,5,1], k = 2))
# log(Solution().putMarbles(weights = [1,4,2,5,2], k = 3))