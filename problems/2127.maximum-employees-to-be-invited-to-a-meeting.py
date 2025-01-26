#
# @lc app=leetcode id=2127 lang=python3
# @lcpr version=30204
#
# [2127] Maximum Employees to Be Invited to a Meeting
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)    # 获取节点个数
        degrees = [0] * n     # 计算每个节点的度
        for f in favorite:
            degrees[f] += 1          # 当前节点 -> f，说明f多了一个入节点，度+1
        q = deque(i for i, d in enumerate(degrees) if d == 0)      # 用于拓扑排序的队列，初始将度为0的节点入队
        max_depth = [1] * n    # 记录这个节点到一个度为0的节点的最大距离，初始为1表示节点本身
        while q:
            id_ = q.popleft() # 获取一个节点
            max_depth[favorite[id_]] = max_depth[id_] + 1  # 节点的指向节点的深度等于节点深度 + 1
            id_ = favorite[id_]  # 更新节点
            degrees[id_] -= 1   # 遍历完一个入节点，度减小1
            if degrees[id_] == 0: q.append(id_)   # 节点度为0，入队，从而得到所有不在环上的节点的最大深度
        
        chain_sum_length = 0     # 环长度为2可以构成的最大链长
        circle_max_length= 0    # 最大环长度
        for i, deg in enumerate(degrees):
            if deg == 0: continue   # 度为0的节点要么是不在环上的节点，要么是在环上但遍历过的节点【即所在环已经遍历过】
            id_ = i             # 记录环的起点
            circle_length = 0    # 每个环长度
            while degrees[id_]:    # 遍历环，直到到达遍历过的点
                circle_length += 1
                degrees[id_] = 0    # 标记环上节点度为0，表示已经遍历过该环
                id_ = favorite[id_]
            if circle_length == 2:
                chain_sum_length += max_depth[id_] + max_depth[favorite[id_]]    # 环长为2，这个环构成的最大链可以拼接到其他环为2的链上
            else:
                circle_max_length= max(circle_max_length, circle_length)   # 环长大于2，更新最大环长
        return max(chain_sum_length, circle_max_length)    # 取二者最大值

# 作者：画图小匠
# 链接：https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/solutions/2511547/javapython3ctuo-bu-pai-xu-fen-lei-tao-lu-pdmo/
        
# @lc code=end



#
# @lcpr case=start
# [2,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,0,1,4,1]\n
# @lcpr case=end

#

