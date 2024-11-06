from collections import Counter
from typing import List


class N:
    value: int
    bit_count: int
    def __init__(self, value: int):
        self.value = value
        self.bit_count = value.bit_count()

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        data = [N(x) for x in nums]
        for i in range(len(data)-1):
            if data[i].value > data[i+1].value:
                if data[i].bit_count != data[i+1].bit_count:
                    return False
                data[i], data[i+1] = data[i+1], data[i]
                j = i
                while j > 0 and data[j-1].value > data[j].value:
                    if data[j-1].bit_count != data[j].bit_count:
                        return False
                    data[j-1], data[j] = data[j], data[j-1]
                    j -= 1
        return True
        


if __name__ == "__main__":
    print(Solution().canSortArray([8,4,2,30,15]))