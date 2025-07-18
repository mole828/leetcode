#
# @lc app=leetcode id=2163 lang=python3
#
# [2163] Minimum Difference in Sums After Removal of Elements
#

# @lc code=start
import heapq
from typing import List


# Time Limit Exceeded
# 4/110 cases passed
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        nums_len = len(nums)
        n = nums_len // 3
        ans_pointer = [float('inf')]
        def dfs(i: int, status: int) -> int:
            if i == nums_len:
                if status.bit_count() != n:
                    return
                arr = []
                for j in range(nums_len):
                    if not status & (1<<j):
                        arr.append(nums[j])
                left, right = arr[:n], arr[n:]
                this_ans = sum(left) - sum(right)
                # print(this_ans, arr, bin(status))
                ans_pointer[0] = min(ans_pointer[0], this_ans)
                return
            pick = status.bit_count()
            if pick < n:
                dfs(i+1, status|(1<<i))
            dfs(i+1, status)

        dfs(0, 0)
        return ans_pointer[0]
            
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 3
        min_h = nums[-n:]
        heapq.heapify(min_h)

        suf_max = [0] * (m - n + 1)  # 后缀最大和
        suf_max[-1] = sum(min_h)
        for i in range(m - n - 1, n - 1, -1):
            suf_max[i] = suf_max[i + 1] + nums[i] - heapq.heappushpop(min_h, nums[i])

        max_h = [-x for x in nums[:n]]  # 所有元素取反，表示最大堆
        heapq.heapify(max_h)

        pre_min = -sum(max_h)  # 前缀最小和
        ans = pre_min - suf_max[n]  # i=n-1 时的答案
        for i in range(n, m - n):
            pre_min += nums[i] + heapq.heappushpop(max_h, -nums[i])
            ans = min(ans, pre_min - suf_max[i + 1])
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-difference-in-sums-after-removal-of-elements/solutions/1247074/qian-zhui-zui-xiao-he-hou-zhui-zui-da-he-yz3d/

# @lc code=end

print(Solution().minimumDifference([3,1,2]))