#
# @lc app=leetcode id=402 lang=python3
# @lcpr version=
#
# [402] Remove K Digits
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start


class Solution:
    # Time Limit Exceeded
    def removeKdigits(self, num: str, k: int) -> str:
        l = len(num) 
        take = l - k 
        def dp(i: int = 0, taked: str = '') -> int: 
            if len(taked) == take:
                return int(taked) if taked else 0 
            if i == l: 
                return float('inf')
            char = num[i] 
            return min(dp(i+1, taked), dp(i+1, taked+char))
        return str(dp())

    # Wrong Answer
    def removeKdigits(self, num: str, k: int) -> str: 
        print(f"removeKdigits({num}, {k})")
        if k == 0:
            return num 
        if k == 1:
            return num[1:]
        begins = [int(num[i]) for i in range(k)]
        i = begins.index(min(begins)) 
        return str(int(num[i] + self.removeKdigits(num[i+1:], k-i)))
        
    def removeKdigits(self, num: str, k: int) -> str: 
        stack = [-float('inf')] 
        for char in num:
            n = int(char) 
            while n < stack[-1] and k: 
                stack.pop() 
                k -= 1 
            stack.append(n) 
        while k: 
            stack.pop() 
            k -= 1
        stack.pop(0) 
        while stack and stack[0]==0:
            stack.pop(0) 
        return ''.join(str(n) for n in stack) if stack else '0'
    

# @lc code=end

print(Solution().removeKdigits(num = "1432219", k = 3))
print(Solution().removeKdigits(num = "10200", k = 1))

#
# @lcpr case=start
# "1432219"\n3\n
# @lcpr case=end

# @lcpr case=start
# "10200"\n1\n
# @lcpr case=end

# @lcpr case=start
# "10"\n2\n
# @lcpr case=end

#

