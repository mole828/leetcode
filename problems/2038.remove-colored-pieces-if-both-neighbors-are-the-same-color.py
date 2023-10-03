#
# @lc app=leetcode id=2038 lang=python3
#
# [2038] Remove Colored Pieces if Both Neighbors are the Same Color
#

# @lc code=start
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_plays, bob_plays = 0, 0
        count = 1 
        
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                count += 1
            else:
                if colors[i - 1] == 'A':
                    alice_plays += max(0, count - 2)
                else:
                    bob_plays += max(0, count - 2)
                count = 1
        
        if colors[-1] == 'A':
            alice_plays += max(0, count - 2)
        else:
            bob_plays += max(0, count - 2)
        
        return alice_plays > bob_plays
# @lc code=end

print(Solution().winnerOfGame("AA"))
print(Solution().winnerOfGame("AAABABB"))
