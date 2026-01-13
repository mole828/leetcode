#
# @lc app=leetcode id=3453 lang=python3
#
# [3453] Separate Squares I
#

# @lc code=start
from bisect import bisect_left
import heapq
from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        max_y = 0
        min_y = float('inf')
        heap = []
        for (_, y, r) in squares:
            heapq.heappush(heap, (y, r, False))
            heapq.heappush(heap, (y + r, -r, False))
            max_y = max(max_y, y + r)
            min_y = min(min_y, y)
        def check(mid_value: float):
            heap_copy = heap.copy()
            heapq.heappush(heap_copy, (mid_value, 0, True))
            left_part = 0
            right_part = 0
            add_to_left = True
            d = 0
            last_y = 0
            while heap_copy:
                y, dd, is_mid = heapq.heappop(heap_copy)
                k = y - last_y
                last_y = y
                if add_to_left:
                    left_part += d * k
                else:
                    right_part += d * k
                d += dd
                if is_mid:
                    add_to_left = False
            # print("left_part", left_part, "right_part", right_part, "mid_value", mid_value)
            return left_part - right_part
        left = min_y
        right = max_y
        mid = (left + right) / 2
        last_check_result = float('inf')
        while left < right:
            check_result = check(mid)
            if check_result < 0:
                left = mid
            else:
                right = mid
            mid = (left + right) / 2
            d_check = abs(check_result - last_check_result)
            if d_check < 1e-6:
                break
            last_check_result = check_result
        return mid
        
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        M = 100_000
        total_area = sum(l * l for _, _, l in squares)

        def check(multi_y: int) -> bool:
            area = 0
            for _, y, l in squares:
                if y * M < multi_y:
                    area += l * min(multi_y - y * M, l * M)
            return area * 2 >= total_area * M

        max_y = max(y + l for _, y, l in squares)
        return bisect_left(range(max_y * M), True, key=check) / M

# @lc code=end

if __name__ == '__main__':
    # print(Solution().separateSquares(squares = [[0,0,1],[2,2,1]]))
    # print(Solution().separateSquares(squares = [[0,0,2],[1,1,1]]))
    print(Solution().separateSquares(squares = [[12,25,3],[3,14,2]]))