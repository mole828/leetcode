#
# @lc app=leetcode id=2322 lang=python3
#
# [2322] Minimum Score After Removals on a Tree
#

# @lc code=start
from functools import reduce
from typing import List


# Time Limit Exceeded, 52/65 cases passed
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        def get_score(cut_status: int) -> int:
            node_to_set: dict[int, set[int]] = {i:set([i]) for i in range(len(nums))}
            for i,edge in enumerate(edges):
                is_cut = cut_status&(1<<i)
                if is_cut:
                    continue
                a, b = edge
                if a in node_to_set and b in node_to_set:
                    set_a = node_to_set[a]
                    set_b = node_to_set[b]
                    new_set = set_a | set_b
                    for k in new_set:
                        node_to_set[k] = new_set
                    continue
                older: set[int] = None
                if a in node_to_set:
                    older = node_to_set[a]
                if b in node_to_set:
                    older = node_to_set[b]
                if older:
                    older.add(a)
                    older.add(b)
                    node_to_set[a] = older
                    node_to_set[b] = older
            all_set = node_to_set.values()
            # print("all_set", all_set, bin(cut_status))
            three_set = {id(s):s for s in all_set}
            values = [reduce(lambda x,y: x^y, [nums[i] for i in s]) for s in three_set.values()]
            max_value = max(values)
            min_value = min(values)
            return max_value - min_value

        min_sorce_pointer = [float("inf")]
        def dfs(i: int = 0, cut_status: int = 0):
            if cut_status.bit_count() == 2:
                score = get_score(cut_status)
                # print(bin(cut_status), score)
                min_sorce_pointer[0] = min(min_sorce_pointer[0], score)
                return
            if i == len(edges):
                return
            dfs(i+1, cut_status)
            dfs(i+1, cut_status|(1<<i))
            
        dfs()
        return min_sorce_pointer[0]
    
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        xor, in_, out = [0] * n, [0] * n, [0] * n
        clock = 0
        def dfs(x: int, fa: int) -> None:
            nonlocal clock
            clock += 1
            in_[x] = clock  # 递
            xor[x] = nums[x]
            for y in g[x]:
                if y != fa:
                    dfs(y, x)
                    xor[x] ^= xor[y]
            out[x] = clock  # 归
        dfs(0, -1)

        # 判断 x 是否为 y 的祖先
        def is_ancestor(x: int, y: int) -> bool:
            return in_[x] < in_[y] <= out[x]

        ans = float("inf")
        # 枚举：删除 x 与 x 父节点之间的边，删除 y 与 y 父节点之间的边
        for x in range(2, n):
            for y in range(1, x):
                if is_ancestor(x, y):  # x 是 y 的祖先
                    a, b, c = xor[y], xor[x] ^ xor[y], xor[0] ^ xor[x]
                elif is_ancestor(y, x):  # y 是 x 的祖先
                    a, b, c = xor[x], xor[x] ^ xor[y], xor[0] ^ xor[y]
                else:  # x 和 y 分别属于两棵不相交的子树
                    a, b, c = xor[x], xor[y], xor[0] ^ xor[x] ^ xor[y]
                ans = min(ans, max(a, b, c) - min(a, b, c))
                if ans == 0:  # 不可能变小
                    return 0  # 提前返回
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-score-after-removals-on-a-tree/solutions/1625899/dfs-shi-jian-chuo-chu-li-shu-shang-wen-t-x1kk/
# @lc code=end

print(Solution().minimumScore(nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]))