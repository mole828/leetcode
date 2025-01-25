#
# @lc app=leetcode id=2948 lang=python3
# @lcpr version=30204
#
# [2948] Make Lexicographically Smallest Array by Swapping Elements
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        res = [0] * len(nums)
        # 先整体按大小排序(保留原始位置), 进而可以根据相邻间隔分组
        ss = sorted([num, i] for i, num in enumerate(nums))
        ss.append([float('inf'), float('inf')]) # 哨兵位

        seg = [ss[0]]
        for idx in range(1, len(ss)):
            # 相邻间隔在limit内就是同一组
            if ss[idx][0] - seg[-1][0] <= limit:
                seg.append(ss[idx])
            else:
                # 将分组内的位置按元素大小排序后重新放置
                for pos, i in enumerate(sorted(pos for _, pos in seg)):
                    res[i] = seg[pos][0]
                seg = [ss[idx]]

        return res

# 作者：desti
# 链接：https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/solutions/2545157/2948-tan-xin-fen-duan-pai-xu-zhong-xin-t-abqg/

# @lc code=end



#
# @lcpr case=start
# [1,5,3,9,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,7,6,18,2,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,7,28,19,10]\n3\n
# @lcpr case=end

#

