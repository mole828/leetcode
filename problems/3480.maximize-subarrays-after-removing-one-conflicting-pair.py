#
# @lc app=leetcode id=3480 lang=python3
# @lcpr version=30204
#
# [3480] Maximize Subarrays After Removing One Conflicting Pair
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        conflict_in_right = [set() for _ in range(n)]
        for a, b in conflictingPairs:
            a,b = min(a,b)-1, max(a,b)-1
            conflict_in_right[a].add(b)
        not_conflict_count = 0
        conflict_once_count = defaultdict(int)
        for left in range(n):
            coming_conflict = set()
            already_conflict = set()
            for right in range(left, n):
                for b in conflict_in_right[right]:
                    coming_conflict.add((right,b))
                need_move = [tup for tup in coming_conflict if tup[1]<=right]
                for tup in need_move:
                    coming_conflict.remove(tup)
                    already_conflict.add(tup)
                if len(already_conflict) == 1:
                    conflict_once_count[list(already_conflict)[0]] += 1
                if not already_conflict:
                    not_conflict_count += 1
        print(conflict_once_count)
        print(not_conflict_count)
        return not_conflict_count + max(conflict_once_count.values())

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        groups = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            groups[a].append(b)

        ans = 0
        extra = [0] * (n + 2)
        b = [n + 1, n + 1]
        for i in range(n, 0, -1):
            b = sorted(b + groups[i])[:2]  # 维护最小 b 和次小 b
            ans += b[0] - i
            extra[b[0]] += b[1] - b[0]

        return ans + max(extra)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximize-subarrays-after-removing-one-conflicting-pair/solutions/3603047/mei-ju-zuo-duan-dian-wei-hu-zui-xiao-ci-4nvu6/
# @lc code=end

# print(Solution().maxSubarrays(4, [[2,3],[1,4]]))
print(Solution().maxSubarrays(25, [[25,18],[2,13],[15,12],[12,15]]))

#
# @lcpr case=start
# 4\n[[2,3],[1,4]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[1,2],[2,5],[3,5]]\n
# @lcpr case=end

#

