#
# @lc app=leetcode id=3508 lang=python3
# @lcpr version=30204
#
# [3508] Implement Router
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import bisect
from collections import defaultdict
from typing import Deque, List


PacketType = tuple[int, int, int]
class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit

        self.packetSet: set[PacketType] = set()
        self.packetQueue = Deque[tuple[int, int, int]]()
        self.destinationDict: dict[int, list[PacketType]] = defaultdict(list)

    def remove(self) -> PacketType:
        (source, destination, timestamp) = self.packetQueue.popleft()
        self.packetSet.remove((source, destination, timestamp))
        self.destinationDict[destination].remove((source, destination, timestamp))
        # print(f"remove {(source, destination, timestamp)}, {self.packetQueue} {self.packetSet}")
        return (source, destination, timestamp)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packetSet:
            return False
        self.packetSet.add(packet)
        if len(self.packetSet) > self.memoryLimit:
            self.remove()
        self.packetQueue.append(packet)
        self.destinationDict[destination].append(packet)
        return True


    def forwardPacket(self) -> List[int]:
        if self.packetSet:
            packet = self.remove()
            return list(packet)
        return []
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = bisect.bisect_left(self.destinationDict[destination], startTime, key=lambda x: x[2])
        right = bisect.bisect_right(self.destinationDict[destination], endTime, lo=left, key=lambda x: x[2])
        return right - left
        
# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
# @lc code=end

r = Router(3)
r.addPacket(1, 4, 90)
r.addPacket(2, 5, 90)
r.addPacket(1, 4, 90)
r.addPacket(3, 5, 95)
r.addPacket(4, 5, 105)
r.forwardPacket()
r.addPacket(5, 2, 110)
r.getCount(5, 100, 110)

#
# @lcpr case=start
# ["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"][[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]\n
# @lcpr case=end

# @lcpr case=start
# ["Router", "addPacket", "forwardPacket", "forwardPacket"][[2], [7, 4, 90], [], []]\n
# @lcpr case=end

#

