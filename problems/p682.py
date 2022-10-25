from bisect import bisect
from typing import List

import numpy


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        value = [0]
        # 单调递增栈+二分 value存放前缀和
        stack = [-1]
        total = 0
        res = numpy.Infinity
        # print(nums)
        for i in range(n):
            # print('i:',i)
            total += nums[i]
            need = total - k
            index = bisect(value, need) - 1
            # print({
            #     'value': value,
            #     'need': need,
            # })
            if index != -1:
                res = min(res, i - stack[index])
            while stack and total <= value[-1]:
                stack.pop()
                value.pop()
            value.append(total)
            stack.append(i)
        return -1 if res == numpy.Infinity else res


if __name__ == '__main__':
    s = Solution()
    print(s.shortestSubarray(nums=[1], k=1))
    print(s.shortestSubarray(nums=[1, 2], k=4))
    print(s.shortestSubarray(nums=[2, -1, 2], k=3))
