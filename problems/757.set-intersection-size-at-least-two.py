#
# @lc app=leetcode id=757 lang=python3
# @lcpr version=30204
#
# [757] Set Intersection Size At Least Two
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from bisect import bisect_left
from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        # 栈中保存闭区间左右端点，栈底到栈顶的区间长度的和
        st = [(-2, -2, 0)]  # 哨兵，保证不和任何区间相交
        for start, end in intervals:
            _, r, s = st[bisect_left(st, (start,)) - 1]
            d = 2 - (st[-1][2] - s)  # 去掉运行中的时间点
            if start <= r:  # start 在区间 st[i] 内
                d -= r - start + 1  # 去掉运行中的时间点
            if d <= 0:
                continue
            while end - st[-1][1] <= d:  # 剩余的 d 填充区间后缀
                l, r, _ = st.pop()
                d += r - l + 1  # 合并区间
            st.append((end - d + 1, end, st[-1][2] + d))
        return st[-1][2]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/set-intersection-size-at-least-two/solutions/3836878/tong-yong-jie-fa-zhan-er-fen-cha-zhao-py-i542/
  
# @lc code=end

# print(Solution().intersectionSizeTwo([[1,3],[3,7],[8,9]]))
print(Solution().intersectionSizeTwo([[1,2],[2,3],[2,4],[4,5]]))

#
# @lcpr case=start
# [[1,3],[3,7],[8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[1,4],[2,5],[3,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,3],[2,4],[4,5]]\n
# @lcpr case=end

#

