class Solution:
    def numTilings(self, n: int) -> int:
        if n==1:return 1
        if n==2:return 2
        f=[[0]*2 for _ in range(n)]
        f[0]=[1,0]
        f[1]=[2,2]
        for i in range(2,n):
            f[i][0]=f[i-1][0]+f[i-2][0]+f[i-1][1]
            f[i][1]=f[i-2][0]*2+f[i-1][1]
        return f[-1][0]%(10**9+7)