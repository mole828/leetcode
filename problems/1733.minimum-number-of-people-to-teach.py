#
# @lc app=leetcode id=1733 lang=python3
#
# [1733] Minimum Number of People to Teach
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages: dict[int, set[int]] = {i+1: set(languages[i]) for i in range(len(languages))}
        chose: dict[int, set[int]] = defaultdict(lambda:set())
        for friendship in friendships:
            u, v = friendship
            u_langs = languages[u]
            v_langs = languages[v]
            if not u_langs.intersection(v_langs):
                chose[u].update(u_langs)
                chose[v].update(v_langs)

        min_teach = float('inf')
        for lang in range(1, n+1):
            teach = 0
            for u in chose:
                if lang not in chose[u]:
                    teach += 1
            min_teach = min(min_teach, teach)
        return min_teach


        
# @lc code=end

print(Solution().minimumTeachings(2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]]))
print(Solution().minimumTeachings(3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]]))
