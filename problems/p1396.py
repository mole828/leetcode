from collections import defaultdict


class UndergroundSystem:
    dictOfSum: defaultdict[str, defaultdict[str, int]]
    dictOfCount: defaultdict[str, defaultdict[str, int]]
    checks: dict[int,tuple[str, int]]
    def __init__(self):
        self.dictOfSum = defaultdict(lambda: defaultdict(lambda:0))
        self.dictOfCount = defaultdict(lambda: defaultdict(lambda:0))
        self.checks = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checks[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checks:
            startStation, tBegin = self.checks[id]
            del self.checks[id]
            self.dictOfSum[startStation][stationName] += t-tBegin
            self.dictOfCount[startStation][stationName] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.dictOfSum[startStation][endStation] / self.dictOfCount[startStation][endStation]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)