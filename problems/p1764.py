import re
from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        return bool(re.search('.*'.join(str(x)[1:-1] for x in groups), str(nums)))