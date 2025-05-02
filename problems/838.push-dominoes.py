#
# @lc app=leetcode id=838 lang=python3
# @lcpr version=30204
#
# [838] Push Dominoes
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        new_state = dominoes
        old_state = ''
        while new_state != old_state:
            old_state = new_state
            new_state_list = list(new_state)
            for i in range(len(old_state)):
                if old_state[i] == '.':
                    fouce = 0
                    if i > 0 and old_state[i-1] == 'R':
                        fouce += 1
                    if i < len(old_state) - 1 and old_state[i+1] == 'L':
                        fouce -= 1
                    if fouce > 0:
                        new_state_list[i] = 'R'
                    elif fouce < 0:
                        new_state_list[i] = 'L'
            new_state = ''.join(new_state_list)
        return new_state
        
# @lc code=end

print(Solution().pushDominoes("RR.L"))
print(Solution().pushDominoes(".L.R...LR..L.."))

#
# @lcpr case=start
# "RR.L"\n
# @lcpr case=end

# @lcpr case=start
# ".L.R...LR..L.."\n
# @lcpr case=end

#

