#
# @lc app=leetcode id=2211 lang=python3
#
# [2211] Count Collisions on a Road
#

# @lc code=start
class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        n = len(directions)
        this_time = []
        this_time_can_move = 0
        for i, d in enumerate(directions):
            this_time.append([d])
            match d:
                case 'S': 
                    pass
                case _:
                    this_time_can_move += 1
        while this_time_can_move:
            next_time = [[] for _ in range(n)]
            next_time_can_move = 0
            for i, car_list in enumerate(this_time):
                for car in car_list:
                    match car:
                        case 'L':
                            if i == 0:
                                pass
                            elif 'R' in this_time[i-1]:
                                ans += 1
                                next_time[i-1].append('S')
                            elif 'S' in this_time[i-1]:
                                ans += 1
                                next_time[i-1].append('S')
                            else:
                                next_time[i-1].append('L')
                                next_time_can_move += 1
                        case 'R':
                            if i == n-1:
                                pass
                            elif 'L' in this_time[i+1]:
                                ans += 1
                                next_time[i+1].append('S')
                            elif 'S' in this_time[i+1]:
                                ans += 1
                                next_time[i+1].append('S')
                            else:
                                next_time[i+1].append('R')
                                next_time_can_move += 1
                        case 'S':
                            next_time[i].append('S')
            this_time = next_time
            this_time_can_move = next_time_can_move
            
        return ans
    
    def countCollisions(self, directions: str) -> int:
        directions = list(directions)
        n = len(directions)
        ans = 0

        # Remove leading 'L's
        i = 0
        while i < n and directions[i] == 'L':
            i += 1

        # Remove trailing 'R's
        j = n - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1

        # Count collisions in the middle segment
        for k in range(i, j + 1):
            if directions[k] != 'S':
                ans += 1

        return ans
# @lc code=end

print(Solution().countCollisions("RLRSLL"))