#
# @lc app=leetcode id=874 lang=python3
# @lcpr version=
#
# [874] Walking Robot Simulation
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        print(obstacle_set)
        direction = complex(0, 1)
        place = [0,0]
        max_distance = 0
        for command in commands:
            if command == -1:
                direction *= complex(0, -1)
            elif command == -2:
                direction *= complex(0, 1)
            else:
                for _ in range(command):
                    if (place[0] + direction.real, place[1] + direction.imag) in obstacle_set:
                        break
                    place[0] += direction.real
                    place[1] += direction.imag
                print(place)
                max_distance = max(max_distance, place[0]**2 + place[1]**2)
        return int(max_distance)
        
# @lc code=end

print(Solution().robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4]]))

#
# @lcpr case=start
# [4,-1,3]\n[]\n
# @lcpr case=end

# @lcpr case=start
# [4,-1,4,-2,4]\n[[2,4]]\n
# @lcpr case=end

# @lcpr case=start
# [6,-1,-1,6]\n[]\n
# @lcpr case=end

#

