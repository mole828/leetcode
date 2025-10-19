#
# @lc app=leetcode id=1625 lang=python3
# @lcpr version=30204
#
# [1625] Lexicographically Smallest String After Applying Operations
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        from collections import deque

        def add(s: str) -> str:
            arr = list(s)
            for i in range(1, len(arr), 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            return ''.join(arr)

        def rotate(s: str) -> str:
            return s[-b:] + s[:-b]

        visited = set()
        queue = deque()
        queue.append(s)
        visited.add(s)
        ans = s

        while queue:
            curr = queue.popleft()
            if curr < ans:
                ans = curr

            added = add(curr)
            if added not in visited:
                visited.add(added)
                queue.append(added)

            rotated = rotate(curr)
            if rotated not in visited:
                visited.add(rotated)
                queue.append(rotated)

        return ans
        
# @lc code=end



#
# @lcpr case=start
# "5525"\n9\n2\n
# @lcpr case=end

# @lcpr case=start
# "74"\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# "0011"\n4\n2\n
# @lcpr case=end

#

