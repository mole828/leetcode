from itertools import accumulate
from typing import List


from itertools import accumulate
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # [9,9,6,0,6,6,9] -> [1,1,-1,-1,-1,-1,1] -> [0, 1, 2, 1, 0, -1, -2, -1]
        # accumulate 累计
        score = list(accumulate([1 if x > 8 else -1 for x in hours], initial=0))
        # 对于每个j,找到最小的i满足i<j且s[i]+1 == s[j]
        stk = []
        for i, x in enumerate(score):
            if len(stk)== 0 or score[stk[-1]] > x :
                stk.append(i)
        # stk: [0,5,6]  到下一个索引前，这个索引是最小的
        ans = 0       
        for i in range(len(hours)-1,-1,-1): # 从后向前数
            while len(stk) > 0 and score[i+1]-score[stk[-1]] > 0:
                dx = i - stk[-1] + 1
                if dx > ans: ans = dx
                stk.pop()
        return ans
        

if __name__ == '__main__':
    Solution().longestWPI([9,9,6,0,6,6,9])
        