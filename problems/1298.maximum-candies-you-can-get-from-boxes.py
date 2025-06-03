#
# @lc app=leetcode id=1298 lang=python3
# @lcpr version=30204
#
# [1298] Maximum Candies You Can Get from Boxes
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        visited = [False] * len(status)
        has_key = [False] * len(status)
        has_box = [False] * len(status)
        for box in initialBoxes:
            has_box[box] = True
        que = initialBoxes.copy()
        while que:
            box = que.pop(0)
            # print(box)
            if visited[box]:
                continue
            if not has_box[box]:
                continue
            if status[box] == 0 and has_key[box] or status[box]==1:
                pass
            else:
                continue
            visited[box] = True
            for key in keys[box]:
                has_key[key] = True
                que.append(key)
            for contained_box in containedBoxes[box]:
                has_box[contained_box] = True
                que.append(contained_box)
        # print(visited)
        return sum(v for idx,v in enumerate(candies) if visited[idx])
                
            
        
# @lc code=end

print(Solution().maxCandies([1,0,1,0], [7,5,4,100], [[],[],[1],[]], [[1,2],[3],[],[]], [0]))

#
# @lcpr case=start
# [1,0,1,0]\n[7,5,4,100]\n[[],[],[1],[]]\n[[1,2],[3],[],[]]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,0,0,0,0]\n[1,1,1,1,1,1]\n[[1,2,3,4,5],[],[],[],[],[]]\n[[1,2,3,4,5],[],[],[],[],[]]\n[0]\n
# @lcpr case=end

#

