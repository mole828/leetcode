#
# @lc app=leetcode id=2503 lang=python3
#
# [2503] Maximum Number of Points From Grid Queries
#

# @lc code=start
import bisect
import heapq
from typing import List

i = complex(0, 1)

class Solution:
    # Time Limit Exceeded, 16/21 cases passed
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        def dfs(querie: int, y: int, x: int, has_meet: set[tuple[int,int]]) -> int:  
            if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]):
                return 0
            if querie <= grid[y][x]:
                return 0
            if (y,x) in has_meet:
                return 0
            has_meet.add((y,x))
            total = 1
            for times in range(4): 
                d = i**times
                total += dfs(querie, int(y + d.real), int(x + d.imag), has_meet)
            return total

        return [dfs(querie, 0, 0, set()) for querie in queries]
    
    # Time Limit Exceeded, 16/21 cases passed
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        mark_matrix = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        def dfs(place: tuple[int,int], has_meet: set[tuple[int,int]], max_value: int): 
            if not (0 <= place[0] < len(grid) and 0 <= place[1] < len(grid[0])):
                return 0
            if place in has_meet:
                return
            new_has_meet = has_meet.copy()
            new_has_meet.add(place)
            new_max_value = max(max_value, grid[place[0]][place[1]])
            old_place_value = mark_matrix[place[0]][place[1]]
            if old_place_value > new_max_value:
                mark_matrix[place[0]][place[1]] = new_max_value
            else:
                return
            # mark_matrix[place[0]][place[1]] = min(mark_matrix[place[0]][place[1]], new_max_value)
            for times in range(4):
                d = i**times
                new_place = (int(place[0] + d.real), int(place[1] + d.imag))
                dfs(new_place, new_has_meet, new_max_value)
        dfs((0,0), set(), 0)
        print(mark_matrix)
        marks = sorted([mark_matrix[i][j] for i in range(len(grid)) for j in range(len(grid[0]))])
        return [bisect.bisect_left(marks, q) for q in queries]
    
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        mark_matrix = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        has_meet: set[tuple[int,int]] = set()
        heap = [(0, 0, 0)]
        heapq.heapify(heap)
        while heap:
            path_max, y, x = heapq.heappop(heap)
            if not (0<=y<len(grid) and 0<=x<len(grid[0])):
                continue
            if (y,x) in has_meet:
                continue
            has_meet.add((y,x))

            grid_value = grid[y][x]
            new_path_max = max(path_max, grid_value)
            mark_matrix[y][x] = new_path_max
            for times in range(4):
                d = i**times
                new_y, new_x = int(y + d.real), int(x + d.imag)
                heapq.heappush(heap, (new_path_max, new_y, new_x))
        # print(mark_matrix)
        flatten = sorted([mark_matrix[i][j] for i in range(len(grid)) for j in range(len(grid[0]))])
        return [bisect.bisect_left(flatten, q) for q in queries]
        
# @lc code=end

print(Solution().maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]))