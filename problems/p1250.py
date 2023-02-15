from functools import reduce
from math import gcd
from typing import List

# 裴蜀定理:
# 若a,b是整数,且gcd(a,b)=d，那么对于任意的整数x,y,ax+by都一定是d的倍数，
# 特别地，一定存在整数x,y，使ax+by=d成立。
# a,b互质的充要条件是存在整数x,y使ax+by=1.

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def mygcd(a,b):
            ans = gcd(a,b)
            print(a,b, ans)
            return ans
        return reduce(mygcd, nums) == 1

    
if __name__ == '__main__':
    Solution().isGoodArray([12,5,7,23])
