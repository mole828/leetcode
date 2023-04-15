from collections import Counter
from functools import cache
from typing import List


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr 

    @cache
    def counter(self, left: int, right: int) -> Counter:
        arr = self.arr[left:right+1]
        return Counter(arr)

    def query(self, left: int, right: int, threshold: int) -> int:
        cot = self.counter(left, right)
        most = cot.most_common(1)[0]
        return -1 if most[1]<threshold else most[0] 



# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)