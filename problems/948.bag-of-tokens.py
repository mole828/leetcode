#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

# @lc code=start
from typing import List

# 没理解题意
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        length = len(tokens)
        def dp(i: int, power: int, score: int) -> int:
            print(f"dp({i},{power},{score})")
            if i == length:
                return score 
            token = tokens[i]
            return max([
                dp(i+1, power-token, score+1) if power > token else 0, 
                dp(i+1, power+token, score-1) if score else 0, 
                dp(i+1, power, score)
            ])
        return dp(0, power, 0)

# Time Limit Exceeded, 102 / 147 testcases passed
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        def dp(left: int, right: int, power: int, score: int) -> int: 
            print({'left':left, 'right':right, 'power':power, 'score':score})
            if left > right:
                return score 
            elif left == right:
                if power >= tokens[left]:
                    return score + 1
                return score
            t_left, t_right = tokens[left], tokens[right]
            return max([
                dp(left+1, right-1, power+(t_right-t_left), score) if power>=t_left else 0,
                dp(left+1, right, power-t_left, score+1) if power>=t_left else 0
            ]) 
        return dp(0, len(tokens)-1, power, 0)
    

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens)-1
        score = 0
        max_score = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score,score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1 
            else:
                break 
        return max_score 

# @lc code=end

print(Solution().bagOfTokensScore([100],50), 0)
print(Solution().bagOfTokensScore([200,100],150), 1)
print(Solution().bagOfTokensScore([100,200,300,400],200), 2)
print(Solution().bagOfTokensScore([71,55,82],54), 0)