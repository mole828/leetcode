#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_table:dict[int,dict[int,int]] = {i:{} for i in range(n)}
        for fromi,toi,pricei in flights:
            flight_table[fromi][toi]=pricei
        @cache
        def find_cheapest_price(src: int, dst: int, k: int):
            if src == dst:
                return 0
            if k<0:
                return float('inf')
            return min(
                (find_cheapest_price(new_src, dst, k-1)+flight_table[src][new_src] for new_src in flight_table[src]),
                default=float('inf')
            )
        price = find_cheapest_price(src, dst, k)
        return -1 if price == float('inf') else price
# @lc code=end

print(Solution().findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))