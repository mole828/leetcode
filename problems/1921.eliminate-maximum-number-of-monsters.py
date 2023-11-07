#
# @lc app=leetcode id=1921 lang=python3
#
# [1921] Eliminate Maximum Number of Monsters
#

# @lc code=start
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_to_city = [dist[i] / speed[i] for i in range(len(dist))]
        time_to_city.sort()
        
        for i in range(len(time_to_city)):

            if time_to_city[i] <= i:
                return i

        return len(dist)
# @lc code=end

