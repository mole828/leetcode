
from functools import cache


def sol(line:str):
    tx, ty, hx, hy = [int(s) for s in line.split()]
    control = set(
        [tuple([hx+dx,hy+dy]) for dx in [-1,1] for dy in [-2,2]] +
        [tuple([hx+dx,hy+dy]) for dx in [-2,2] for dy in [-1,1]] +
        [tuple([hx, hy])]
    )
    @cache
    def dp(x:int, y:int)->int:
        if tuple([x,y]) in control:
            return 0
        if x>tx or y>ty:
            return 0
        if x==tx and y==ty:
            return 1
        return sum([
            dp(x+1, y),
            dp(x, y+1)
        ])
    print(dp(0,0))

if __name__ == '__main__':
    sol(input())