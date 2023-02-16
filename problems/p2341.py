from collections import Counter
from functools import reduce
from typing import List


import numpy as np

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        return reduce(
            lambda a,b:a+b,
            [np.array([x//2,x%2]) for x in Counter(nums).values()]
        ).tolist()


if __name__ == '__main__':
    print(Solution().numberOfPairs(nums = [1,3,2,1,3,2,2]))
