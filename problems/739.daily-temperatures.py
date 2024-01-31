#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
from collections import deque
from typing import List

# Time Limit Exceeded
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        answer = [0] * length
        for i in range(length):
            vi = temperatures[i]
            count = 1 
            for j in range(i+1, length):
                vj = temperatures[j]
                if vj > vi:
                    break 
                count += 1
            else:
                count = 0
            answer[i] = count
        return answer
    

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        deq = deque()
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            if not deq:
                deq.appendleft(i)
                res[i] = 0
            else:
                while deq and temperatures[i] >= temperatures[deq[0]]:
                    deq.popleft()

                if not deq:
                    res[i] = 0
                else:
                    res[i] = deq[0] - i

                deq.appendleft(i)
            print(deq)

        return res
    
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        deq = deque() 
        answer = [0] * length

        for i in range(length-1,-1,-1):
            if deq:
                pass
                while deq and temperatures[i] >= temperatures[deq[0]]:
                    deq.popleft()
                if not deq:
                    answer[i] = 0
                else:
                    answer[i] = deq[0] - i 
                deq.appendleft(i)
            else:
                deq.appendleft(i)
                answer[i] = 0
        return answer
# @lc code=end

print(Solution().dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))