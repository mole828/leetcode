#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
from collections import Counter, defaultdict
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def mark(edges: List[List[int]]) -> dict[int, int]:
            res: dict[int, int] = {}
            link_table: dict[int, set[int]] = defaultdict(set)
            for a,b in edges:
                link_table[a].add(b)
                link_table[b].add(a)
            que = [(0, 0)]
            while que:
                i, shoud_mark = que.pop(0)
                if i in res:
                    continue
                res[i] = shoud_mark
                next_shoud_mark = 1 - shoud_mark
                for next_i in link_table[i]:
                    que.append((next_i, next_shoud_mark))
            return res
        mark1 = mark(edges1)
        count1 = Counter(mark1.values())
        mark2 = mark(edges2)
        count2 = Counter(mark2.values())
        max_of_count2 = max(count2.values())
        return [count1[mark1[i]] + max_of_count2 for i in sorted(mark1.keys())]

# @lc code=end

print(Solution().maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]))