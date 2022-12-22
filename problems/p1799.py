from typing import List

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a%b
    return a

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m=len(nums)
        maxL=1<<m
        ans=[0]*maxL
        for i in range(1,maxL):
            k=bin(i).count('1')
            if not k&1:
                bits=[j for j in range(m) if i&(1<<j)]
                for a in bits:
                    for b in bits:
                        if a!=b:
                            ans[i]=max(ans[i],ans[i^(1<<a)^(1<<b)]+gcd(nums[a],nums[b])*k//2)
        return ans[maxL-1]

if __name__ == '__main__':
    print(gcd(24,36))