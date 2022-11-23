from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxs = defaultdict(lambda:0)
        for x in range(lowLimit,highLimit+1):boxs[sum(int(s) for s in str(x))]+=1
        return max(boxs.values())
        

if __name__ == '__main__':
    Solution().countBalls(1,10)