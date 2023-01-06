class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for x in range(1,num+1):
            su = sum( int(s) for s in str(x) )
            if su%2 == 0:
                ans+=1
        return ans