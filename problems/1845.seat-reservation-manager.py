#
# @lc app=leetcode id=1845 lang=python3
#
# [1845] Seat Reservation Manager
#

# @lc code=start
from bisect import bisect_left
import heapq


class SeatManager:
    __seats: list[int]
    def __init__(self, n: int):
        self.__seats = [] 
        for i in range(1,n+1):
            heapq.heappush(self.__seats, i) 

    def reserve(self) -> int:
        return heapq.heappop(self.__seats)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.__seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# @lc code=end

