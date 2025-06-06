#
# @lc app=leetcode id=2434 lang=python3
#
# [2434] Using a Robot to Print the Lexicographically Smallest String
#

# @lc code=start
import heapq


class Solution:
    # Memory Limit Exceeded, 23/62 cases passed
    def robotWithString0(self, s: str) -> str:
        que: list[tuple[list[str], list[str], list[str]]] = [([],[],list(s))]
        heapq.heapify(que)
        while que:
            old_p, old_t, old_s = heapq.heappop(que)
            if not old_s and not old_t:
                return ''.join(old_p)
            # print(old_p)
            if old_t:
                new_t = old_t.copy()
                new_p = old_p.copy()
                new_p.append(new_t.pop())
                heapq.heappush(que, (new_p, new_t, old_s))
            if old_s:
                new_s = old_s.copy()
                new_t = old_t.copy()
                new_t.append(new_s.pop(0))
                heapq.heappush(que, (old_p, new_t, new_s))
        raise Exception("not found")

    def robotWithString(self, s: str) -> str:
        n = len(s)
        suf_min = ['z'] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf_min[i] = min(suf_min[i + 1], s[i])

        ans: list[str] = []
        st: list[str] = []
        for i, ch in enumerate(s):
            st.append(ch)
            while st and st[-1] <= suf_min[i + 1]:
                ans.append(st.pop())
        return ''.join(ans)

# @lc code=end

# print(Solution().robotWithString(s = "zza"))
print(Solution().robotWithString(s = "bdda"))