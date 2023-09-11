#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        data: defaultdict[any,List[int]] = defaultdict(list)
        for index in range(len(groupSizes)):
            size = groupSizes[index]
            data[size].append(index) 
        ans = []
        for size in data.keys():
            arr = data[size]
            for v in [arr[i:i+size] for i in range(0, len(arr), size)]:
                ans.append(v)            
        return ans
# @lc code=end

