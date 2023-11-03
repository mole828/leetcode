#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        options = []
        has = [i for i in range(1,n+1)]
        while target:
            a = has.pop(0) 
            if a == target[0]:
                target.pop(0)
                options.append("Push")
            else:
                options.append("Push")
                options.append("Pop")
        return options
    
# @lc code=end

