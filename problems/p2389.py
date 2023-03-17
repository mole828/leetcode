from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        summary = 0
        maxmap = {q:len(nums) for q in queries}
        sortedqueries = sorted(queries)
        for i in range(len(nums)):
            summary += nums[i]
            while len(sortedqueries)!=0 and summary>sortedqueries[0]:
                k = sortedqueries.pop(0)
                maxmap[k] = i
        return [maxmap[k] for k in queries]