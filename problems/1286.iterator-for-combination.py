#
# @lc app=leetcode id=1286 lang=python3
#
# [1286] Iterator for Combination
#

# @lc code=start
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        characters_length = len(characters)
        arr = []
        def dfs(s: str, i: int):
            if i == characters_length:
                return
            c = characters[i]
            if len(s) == combinationLength - 1:
                arr.append(s+c)
            dfs(s+c, i+1)
            dfs(s, i+1)
        dfs('',0)
        self.arr = arr

    def next(self) -> str:
        return self.arr.pop(0)

    def hasNext(self) -> bool:
        return bool(self.arr)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

CombinationIterator('abc',2)