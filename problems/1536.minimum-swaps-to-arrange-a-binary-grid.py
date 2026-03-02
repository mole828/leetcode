#
# @lc app=leetcode id=1536 lang=python3
#
# [1536] Minimum Swaps to Arrange a Binary Grid
#

# @lc code=start
from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def tailZeros(row: int) -> int:
            _row = grid[row]
            try:
                return _row[::-1].index(1)
            except ValueError:
                return n
        swap_time = 0
        has_swapped = True
        while has_swapped:
            has_swapped = False
            for row in range(n-1):
                z0 = tailZeros(row)
                z1 = tailZeros(row+1)
                print(z0, z1)
                if z0 < z1:
                    grid[row], grid[row+1] = grid[row+1], grid[row]
                    swap_time += 1
                    has_swapped = True
        print("print grid")
        for row in range(n):
            z = tailZeros(row)
            print(grid[row], z)
            if z < n - row - 1:
                return -1
        return swap_time
        
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tail_zeros = [n] * n
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    tail_zeros[i] = n - 1 - j
                    break

        ans = 0
        for i in range(n - 1):
            need_zeros = n - 1 - i
            for j in range(i, n):
                if tail_zeros[j] >= need_zeros:
                    ans += j - i
                    tail_zeros[i + 1: j + 1] = tail_zeros[i: j]
                    break
            else: 
                return -1
        return ans

# @lc code=end

if __name__ == "__main__":
    # print(Solution().minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]))
    print(Solution().minSwaps([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]))