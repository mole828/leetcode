#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#

# @lc code=start
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack:list[str|int] = ['']
        cArray = [c for c in s]
        def stackLength() -> int:
            ans = 0
            for v in stack:
                if type(v) is str:
                    ans += len(v)
                    continue
                ans *= v 
            return ans 
            
        while cArray:
            c = cArray.pop(0)
            try:
                ic = int(c)
                stack.append(ic)
                if stackLength() > k:
                    break 
            except ValueError:
                if not stack or type(stack[-1]) is int:
                    stack.append('')
                stack[-1] += c 
            
        
        print(stack)
        l2 = stackLength()
        while stack:
            last = stack.pop()
            l1 = stackLength()
            print(stack, last, l1, l2, k)
            if l1 < k <= l2:
                if type(last) is str:
                    return last[k-l1-1]
                if type(last) is int:
                    if k == l2:
                        k = l1 
                    else: 
                        k = k % l1 
                        if k==0:
                            k = l1
            l2 = l1 


# @lc code=end
print(Solution().decodeAtIndex(s = "leet2code3", k = 10))
print(Solution().decodeAtIndex(s = "ha22", k = 5))
print(Solution().decodeAtIndex(s = "a23", k = 6))
print(Solution().decodeAtIndex(s = "a2b3c4d5e6f7g8h9", k = 9))
print(Solution().decodeAtIndex(s = "vk6u5xhq9v", k = 554))