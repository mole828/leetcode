from itertools import product
from math import log


class Solution:
    def powerfulIntegers(self, x, y, bound):
        res = []
        rg = int(log(max(bound, 1), min(max(x, 2), max(y, 2))))+1
        for i, j in product(range(rg), repeat=2):
            print(i,j)
            num = x ** i + y ** j
            if num <= bound:
                res.append(num)
        return list(set(res))
    

if __name__ == '__main__':
    assert Solution().powerfulIntegers(x = 2, y = 3, bound = 10) == [2,3,4,5,7,9,10]

'''
学到了, product函数
'''