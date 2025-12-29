#
# @lc app=leetcode id=756 lang=python3
#
# [756] Pyramid Transition Matrix
#

# @lc code=start
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        bottom = list(bottom)
        n = len(bottom)
        allowed_map: dict[tuple[str,str], list[str]] = {}
        for triplet in allowed:
            key = (triplet[0], triplet[1])
            if key not in allowed_map:
                allowed_map[key] = []
            allowed_map[key].append(triplet[2])
        def backtrack(curr: list[str], last: list[str]) -> bool:
            if len(last) == 1:
                return True
            if len(curr) + 1 == len(last):
                return backtrack([], last = curr)
            level = len(last)
            key = (last[len(curr)], last[len(curr) + 1])
            if key not in allowed_map:
                return False
            for c in allowed_map[key]:
                curr.append(c)
                if backtrack(curr, last):
                    return True
                curr.pop()
            return False
        return backtrack(curr = [], last = bottom)
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.pyramidTransition(bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]))  # True
    print(solution.pyramidTransition(bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]))