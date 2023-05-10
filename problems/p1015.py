class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        p = 0
        for i in range(1,100000):
            p=(p*10+1)%k
            if p==0:return i
        return -1