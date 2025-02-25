#
# @lc app=leetcode id=1524 lang=python3
#
# [1524] Number of Sub-arrays With Odd Sum
#

# @lc code=start
from collections import Counter
from typing import List

def log(*args):
    # print(*args)
    pass

class Solution:
    def numOfSubarrays(self, arr: List[int]):
        arr = [x%2 for x in arr]
        log(arr)
        count2here = [0]
        for x in arr:    
            count2here.append(count2here[-1] + x)
        log(count2here)
        counter = Counter(count2here)
        count = 0
        for left in range(len(count2here)):
            left_value = count2here[left]
            # for right in range(left, len(count2here)):
            #     right_value = count2here[right]
            #     if (right_value - left_value) % 2:
            #         log(left_value, right_value)
            #         count += 1
            right_value = left_value + 1
            while inc:=counter[right_value]:
                count += inc
                right_value += 2

        return count % (10**9 + 7)
    
class Solution:
    def numOfSubarrays(self, arr: List[int]):
        count2here = [0]
        for x in arr:    
            count2here.append(count2here[-1] + x%2)
        odd, even = 0, 0
        new_arr = []
        for x in count2here:
            y = x % 2
            if y:
                odd += 1
            else:
                even += 1
            new_arr.append(y)
        log(odd, even, new_arr)
        count = 0
        for x in new_arr:
            if x:
                count += even
                odd -= 1
            else:
                count += odd
                even -= 1
        return count % (10**9 + 7)
 
# @lc code=end

print(Solution().numOfSubarrays([1,3,5]))