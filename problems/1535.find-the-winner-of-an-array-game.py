#
# @lc app=leetcode id=1535 lang=python3
#
# [1535] Find the Winner of an Array Game
#

# @lc code=start
from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        if k >= len(arr):
            return max(arr)
        
        current_winner = arr[0]
        consecutive_wins = 0
        
        for i in range(1, len(arr)):
            if current_winner > arr[i]:
                consecutive_wins += 1
            else:
                current_winner = arr[i]
                consecutive_wins = 1
            
            if consecutive_wins == k:
                return current_winner
        
        return current_winner
# @lc code=end

