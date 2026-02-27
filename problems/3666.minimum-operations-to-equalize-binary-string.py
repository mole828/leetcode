#
# @lc app=leetcode id=3666 lang=python3
#
# [3666] Minimum Operations to Equalize Binary String
#
import heapq
# @lc code=start
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zero = s.count('0')
        one = n - zero
        que = [(0, zero, one)]
        has_meet = set()
        while que:
            step, z, o = heapq.heappop(que)
            # print(z,o,step,que)
            if (z,o) in has_meet:
                continue
            has_meet.add((z,o))
            if z == 0:
                return step
            # 选择思路错误？
            for flip_0_to_1 in range(max(0, k - o), min(k, z) + 1):
                flip_1_to_0 = k - flip_0_to_1
                
                # 计算新状态
                new_z = z - flip_0_to_1 + flip_1_to_0
                new_o = o + flip_0_to_1 - flip_1_to_0
                
                # 将新状态加入队列
                # que.append((new_z, new_o, step + 1))
                heapq.heappush(que, (step + 1, new_z, new_o))
        return -1

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        not_vis = [SortedList(range(0, n + 1, 2)), SortedList(range(1, n + 1, 2))]
        not_vis[0].add(n + 1)  # 哨兵，下面 sl[idx] <= mx 无需判断越界
        not_vis[1].add(n + 1)

        start = s.count('0')  # 起点
        not_vis[start % 2].discard(start)
        q = [start]
        ans = 0
        while q:
            tmp = q
            q = []
            for z in tmp:
                if z == 0:  # 没有 0，翻转完毕
                    return ans
                # not_vis[mn % 2] 中的从 mn 到 mx 都可以从 z 翻转到
                mn = z + k - 2 * min(k, z)
                mx = z + k - 2 * max(0, k - n + z)
                sl = not_vis[mn % 2]
                idx = sl.bisect_left(mn)
                while sl[idx] <= mx:
                    j = sl.pop(idx)  # 注意 pop(idx) 会使后续元素向左移，不需要写 idx += 1
                    q.append(j)
            ans += 1
        return -1

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-operations-to-equalize-binary-string/solutions/3768129/shu-xue-zuo-fa-pythonjavacgo-by-endlessc-ol6s/
# @lc code=end

if __name__ == "__main__":
    # print(Solution().minOperations("0101",3))
    # print(Solution().minOperations("110",1))
    # print(Solution().minOperations("101",2))
    print(Solution().minOperations("101",3))