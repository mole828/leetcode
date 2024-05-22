#
# @lc app=leetcode id=131 lang=python3
# @lcpr version=
#
# [131] Palindrome Partitioning
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class dict_tree(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

class Solution:
    def is_palindrome(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] != s[-i-1]:
                return False
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        def build(s: str) -> dict_tree:
            node = {}
            if not s:
                return node
            for l in range(len(s)):
                left = s[:l+1]
                right = s[l+1:]
                if self.is_palindrome(left):
                    node[left] = build(right)
            return node
        root = build(s)
        # print(root)
        def dfs(node: dict_tree, path: List[str], result: List[List[str]]):
            if not node:
                result.append(path)
                return
            for key in node:
                dfs(node[key], path + [key], result)
        result = []
        dfs(root, [], result)
        return result
        
            
# @lc code=end

print(Solution().partition("aab"))

#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#

