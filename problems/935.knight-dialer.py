#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#

# @lc code=start
from collections import Counter
from functools import cache


class Solution:
    __board = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [False,0,False],
    ]
    @cache
    def __next_place(xy: tuple[int,int]) -> list[tuple[int,int]]:
        next_place = []
        x,y = xy 
        for dx in [-2,-1,1,2]:
            for dy in [-2,-1,1,2]:
                if abs(dx) != abs(dy):
                    tx,ty = x+dx, y+dy 
                    if ty < 0 or ty >= len(Solution.__board):
                        continue
                    if tx < 0 or tx >= 3:
                        continue
                    value = Solution.__board[ty][tx]
                    if not value is False:
                        next_place.append((tx,ty))
        # print(f"{xy} => {next_place}")
        return next_place
    @cache
    def __in(xy: tuple[int,int]):
        x,y= xy 
        return Solution.__board[y][x]
    @cache
    def __place(num: int) -> tuple[int,int]:
        for y,row in enumerate(Solution.__board):
            for x,v in enumerate(row):
                if v is num:
                    return (x,y)

    def knightDialer(self, n: int) -> int:
        # print(Solution.__next_place((1,1)))
        # print(Solution.__place(0))
        max_deep = n

        @cache
        def dp(deep: int, xy: tuple[int,int]) -> int:
            if deep == max_deep:
                # print(s+str(Solution.__in(xy)))
                return 1
            return sum(
                dp(deep+1, new_place) 
                for new_place in Solution.__next_place(
                    xy
                )
            )
        
        return sum(
            dp(1, Solution.__place(num)) for num in range(10)
        ) % (10**9 + 7)
# @lc code=end
print(Solution().knightDialer(2))