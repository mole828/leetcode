#
# @lc app=leetcode id=2483 lang=python3
#
# [2483] Minimum Penalty for a Shop
#

# @lc code=start
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        countY = customers.count("Y")
        minPenalty = countY
        bestHour = 0
        currentPenalty = countY
        for i, c in enumerate(customers):
            if c == "Y":
                currentPenalty -= 1
            else:
                currentPenalty += 1
            if currentPenalty < minPenalty:
                minPenalty = currentPenalty
                bestHour = i + 1
        return bestHour
# @lc code=end

