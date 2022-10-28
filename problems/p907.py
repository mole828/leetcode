from typing import List
from sortedcontainers import SortedList

class Solution:
    mod = 10 ** 9 + 7
    def sumSubarrayMins(self, arr: List[int]) -> int:
        length = len(arr)
        s = 0
        before = sorted(range(length), key=lambda x: arr[x])
        after = SortedList((-1, length))
        print(arr, before)
        for i in before:
            index = after.bisect(i)
            print(f'{before}[{i}]=>{index}')
            after.add(i)
            ad = arr[i] * (i - after[index-1]) * (after[index+1] - i)
            s += ad
        return s % (Solution.mod)

if __name__ == '__main__':
    Solution().sumSubarrayMins([3,1,2,4])
    Solution().sumSubarrayMins([11,81,94,43,3])