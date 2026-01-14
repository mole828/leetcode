#
# @lc app=leetcode id=3454 lang=python3
#
# [3454] Separate Squares II
#

# @lc code=start
from bisect import bisect_left
import heapq
from itertools import pairwise
from typing import List, TypeVar

T = TypeVar("T")
class SegmentTree[T: int | float]:
    data: List[tuple[T, T]]
    heap: List[tuple[T, bool]]
    def add(self, _range: tuple[T, T]):
        left, right = _range
        heapq.heappush(self.heap, (left, True))
        heapq.heappush(self.heap, (right, False))
    def out(self, _range: tuple[T, T]):
        heapq.heappush(self.heap, (_range[0], False))
        heapq.heappush(self.heap, (_range[1], True))

    
    def __init__(self, data: List[tuple[T, T]] = []):
        self.data = data
        self.heap = []
        for tup in data:
            self.add(tup)

    def sum(self) -> T:
        heap = self.heap.copy()
        total = 0
        now = 0
        last: T | None = None
        while heap:
            val, is_add = heapq.heappop(heap)
            if last:
                total += now * (val - last)
            if is_add:
                now += val
            else:
                now -= val
            last = val
        return total
    
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        M = 100000
        y_heap = []
        for id, (x, y, l) in enumerate(squares):
            heapq.heappush(y_heap, (y, x, x+l, True, id))
            heapq.heappush(y_heap, (y+l, x, x+l, False, id))
        total_area = 0
        y_heap_copy = y_heap.copy()
        x_tree = SegmentTree[int]()
        y_heap_copy = y_heap.copy()
        last: int|None = None
        print(y_heap)
        while y_heap_copy:
            y, x_left, x_right, is_add, id = heapq.heappop(y_heap_copy)
            if last:
                total_area += x_tree.sum() * (y - last)
            if is_add:
                x_tree.add((x_left, x_right))
            else:
                x_tree.out((x_left, x_right))
        print("total_area", total_area)
        return total_area


class Node:
    __slots__ = 'l', 'r', 'min_cover_len', 'min_cover', 'todo'

    def __init__(self):
        self.l = 0
        self.r = 0
        self.min_cover_len = 0  # 区间内被矩形覆盖次数最少的底边长之和
        self.min_cover = 0      # 区间内被矩形覆盖的最小次数
        self.todo = 0           # 子树内的所有节点的 min_cover 需要增加的量，注意这可以是负数


class SegmentTree:
    def __init__(self, xs: List[int]):
        n = len(xs) - 1  # xs.size() 个横坐标有 xs.size()-1 个差值
        self.seg = [Node() for _ in range(2 << (n - 1).bit_length())]
        self.build(xs, 1, 0, n - 1)

    def get_uncovered_length(self) -> int:
        return 0 if self.seg[1].min_cover else self.seg[1].min_cover_len

    # 根据左右儿子的信息，更新当前节点的信息
    def maintain(self, o: int) -> None:
        lo = self.seg[o * 2]
        ro = self.seg[o * 2 + 1]
        mn = min(lo.min_cover, ro.min_cover)
        self.seg[o].min_cover = mn
        # 只统计等于 min_cover 的底边长之和
        self.seg[o].min_cover_len = (lo.min_cover_len if lo.min_cover == mn else 0) + \
                                    (ro.min_cover_len if ro.min_cover == mn else 0)

    # 仅更新节点信息，不下传懒标记 todo
    def do(self, o: int, v: int) -> None:
        self.seg[o].min_cover += v
        self.seg[o].todo += v

    # 下传懒标记 todo
    def spread(self, o: int) -> None:
        v = self.seg[o].todo
        if v:
            self.do(o * 2, v)
            self.do(o * 2 + 1, v)
            self.seg[o].todo = 0

    # 建树
    def build(self, xs: List[int], o: int, l: int, r: int) -> None:
        self.seg[o].l = l
        self.seg[o].r = r
        if l == r:
            self.seg[o].min_cover_len = xs[l + 1] - xs[l]
            return
        m = (l + r) // 2
        self.build(xs, o * 2, l, m)
        self.build(xs, o * 2 + 1, m + 1, r)
        self.maintain(o)

    # 区间更新
    def update(self, o: int, l: int, r: int, v: int) -> None:
        if l <= self.seg[o].l and self.seg[o].r <= r:
            self.do(o, v)
            return
        self.spread(o)
        m = (self.seg[o].l + self.seg[o].r) // 2
        if l <= m:
            self.update(o * 2, l, r, v)
        if m < r:
            self.update(o * 2 + 1, l, r, v)
        self.maintain(o)


# 代码逻辑同 850 题，增加一个 records 数组记录关键数据
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        xs = []
        events = []
        for lx, y, l in squares:
            rx = lx + l
            xs.append(lx)
            xs.append(rx)
            events.append((y, lx, rx, 1))
            events.append((y + l, lx, rx, -1))

        # 排序，方便离散化
        xs = sorted(set(xs))

        # 初始化线段树
        t = SegmentTree(xs)

        # 模拟扫描线从下往上移动
        events.sort(key=lambda e: e[0])
        records = []
        tot_area = 0
        for (y, lx, rx, delta), e2 in pairwise(events):
            l = bisect_left(xs, lx)  # 离散化
            r = bisect_left(xs, rx) - 1  # r 对应着 xs[r] 与 xs[r+1]=rx 的差值
            t.update(1, l, r, delta)  # 更新被 [lx, rx] 覆盖的次数
            sum_len = xs[-1] - xs[0] - t.get_uncovered_length()  # 减去没被矩形覆盖的长度
            records.append((tot_area, sum_len))  # 记录关键数据
            tot_area += sum_len * (e2[0] - y)  # 新增面积 = 被至少一个矩形覆盖的底边长之和 * 矩形高度

        # 二分找最后一个 < tot_area / 2 的面积
        i = bisect_left(records, tot_area, key=lambda r: r[0] * 2) - 1
        area, sum_len = records[i]
        return events[i][0] + (tot_area - area * 2) / (sum_len * 2)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/separate-squares-ii/solutions/3078402/lazy-xian-duan-shu-sao-miao-xian-pythonj-eeqk/


# @lc code=end

if __name__ == '__main__':
    # print(Solution().separateSquares(squares = [[0,0,1],[2,2,1]]))
    print(Solution().separateSquares(squares = [[0,0,2],[1,1,1]]))
    # print(Solution().separateSquares(squares = [[12,25,3],[3,14,2]]))