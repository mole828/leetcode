from functools import lru_cache

n = int(input())
matrix = [[0] * n for _ in range(n)]
xy2i = {}
for i in range(2**31):  # 我这里只循环10次，你需要根据实际情况修改
    x, y, value = map(int, input().split())
    if x == y == value == 0:
        break
    x-=1
    y-=1
    matrix[x][y] = value
    xy2i[(x, y)] = i
# print(matrix, xy2i)
def mhas(mask: int, xy) -> bool:
    if xy not in xy2i:
        return False
    id = xy2i[xy]
    return not bool(mask & (1 << id))

def mdis(mask: int, xy) -> int:
    id = xy2i[xy]
    return mask | (1 << id)

@lru_cache
def f(x, y, mask, remaining_rounds):
    if x == n or y == n:
        return 0
    if x == y == n-1:
        if remaining_rounds > 1:
            return f(0, 0, mask, remaining_rounds - 1)
        else:
            return 0
    ans = 0
    xy = (x,y)
    if mhas(mask, xy):
        mask = mdis(mask, xy)
        ans += matrix[x][y]
    ans += max(f(x + 1, y, mask, remaining_rounds), f(x, y + 1, mask, remaining_rounds))
    return ans

print(f(0, 0, 0, 2))

# TODO