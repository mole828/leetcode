#
# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for y in range(1, query_row+1):
            next_row = [0]*(y+1)
            for j, volume in enumerate(row):
                if volume > 1:
                    next_row[j] += (volume - 1) / 2
                    next_row[j + 1] += (volume - 1) / 2
            row = next_row
            
        return min(1, row[query_glass])
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.champagneTower(1, 1, 1))
    print(s.champagneTower(2, 1, 1))
    print(s.champagneTower(100000009, 33, 17))