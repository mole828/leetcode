class Solution:
    def baseNeg2(self, n: int) -> str:
        res = ''
        print(n)
        while n:
            n, k = -(n // 2), n % 2
            res = str(k)+res
            print(n,k,res)
        return res if res else '0'
    
if __name__ == '__main__':
    Solution().baseNeg2(7)