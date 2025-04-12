#
# @lc app=leetcode id=3272 lang=python3
# @lcpr version=30204
#
# [3272] Find the Count of Good Integers
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from math import factorial
from typing import List


class Solution:
    def isPalindrome(self, n: int) -> bool:
        s = str(n)
        return s == s[::-1]
    def rearranged(self, n: int):
        def dp(path: str, last: List[str]):
            if len(last) == 0 and path[0] != '0':
                yield int(path)
            
            for i in range(len(last)):
                c = last.pop(i)
                for v in dp(path + c, last):
                    yield v
                last.insert(i, c)
            
        for v in dp('', last=[c for c in str(n)]):
            yield v
    
    # time limit exceeded, 2 / 90 testcases passed
    def countGoodIntegers(self, n: int, k: int) -> int:
        left = 10**(n-1)
        right = 10**n
        result: set[int] = set()
        for i in range(left, right):
            for re in self.rearranged(i):
                if re % k == 0 and self.isPalindrome(re):
                    result.add(i)
                
        # print(sorted(result))
        return len(result)
    
    # time limit exceeded, 54 / 90 testcases passed
    def countGoodIntegers(self, n: int, k: int) -> int:
        left = 10**(n-1)
        right = 10**n
        need_rearrange = []
        for i in range(left, right):
            if i % k == 0 and self.isPalindrome(i):
                need_rearrange.append(i)
        print("need_rarraged finished")
        result = set()
        for i in need_rearrange:
            for re in self.rearranged(i):
                result.add(re)
        # print(sorted(result))
        return len(result)
            
    def countGoodIntegers(self, n: int, k: int) -> int:
        dictionary = set()
        base = 10 ** ((n-1)//2)
        skip = n & 1
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            palindromicInteger = int(s)
            if palindromicInteger % k == 0:
                sorted_s = ''.join(sorted(s))
                dictionary.add(sorted_s)
        print(dictionary)
        fac = [factorial(i) for i in range(n+1)] 
        # factorial 阶乘
        ans = 0
        for s in dictionary:
            cnt = [0] * 10
            for c in s:
                cnt[int(c)] += 1
            # 通过阶乘计算n位数排列总量, 去除相同数字的重复排列
            total = (n-cnt[0]) * fac[n-1]
            for x in cnt:
                total //= fac[x]
            ans += total
        return ans
# @lc code=end

print(Solution().countGoodIntegers(3, 5))
print(Solution().countGoodIntegers(1,4))
# print(Solution().countGoodIntegers(5,6))

#
# @lcpr case=start
# 3\n5\n
# @lcpr case=end

# @lcpr case=start
# 1\n4\n
# @lcpr case=end

# @lcpr case=start
# 5\n6\n
# @lcpr case=end

#

