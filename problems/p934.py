from typing import List, Tuple
import numpy

class Solution:
    grid: List[List[int]]

    def shortestBridge(self, grid: List[List[int]]) -> int:
        print(numpy.mat(grid))

        dfsStack: List[Tuple[int, int]] = []
        to = 2

        def dfs(y: int, x: int):
            tup = (y, x)
            if tup in dfsStack:
                return
            dfsStack.append(tup)
            for (dy, dx) in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ty = max(0, min(y+dy, len(grid)-1))
                tx = max(0, min(x+dx, len(grid[y])-1))
                if grid[y][x] != grid[ty][tx]:
                    continue
                dfs(ty, tx)
            dfsStack.remove(tup)
            grid[y][x] = to

        def first(target: int):
            for y in range(len(grid)):
                row = grid[y]
                for x in range(len(row)):
                    i = row[x]
                    if i == target:
                        return y, x
        dfs(*first(1))

        def grow(target: int = 1) -> bool:
            growStack: List[Tuple[int, int]] = []
            for y in range(len(grid)):
                row = grid[y]
                for x in range(len(row)):
                    if row[x] == target:
                        tup = (y, x)
                        growStack.append(tup)
            for (y, x) in growStack:
                for (dy, dx) in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ty = max(0, min(y+dy, len(grid)-1))
                    tx = max(0, min(x+dx, len(grid[y])-1))
                    if grid[ty][tx] == to:
                        return True
                    grid[ty][tx] = 1

        i = 0
        while not grow():
            i += 1
            print('grow', i)
            print(numpy.mat(grid))

        return i


if __name__ == '__main__':
    print(__name__)
    s = Solution()
    print(
        [(y, x) for y in [-1, 1] for x in [-1, 1]]
    )
    s.shortestBridge(grid=[
        [0, 1],
        [1, 0],
    ])
    s.shortestBridge(grid=[
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 1]
    ])
    s.shortestBridge(grid=[
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ])
