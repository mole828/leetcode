import heapq


class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        class Order(object):
            def __init__(self, price, amount, otype):
                self.p = price
                self.a = amount
                self.t = otype
            def __lt__(self, other):
                return self.p < other.p if self.t == 1 else self.p > other.p
        bq, sq = [], []
        x = 0
        while x < len(orders):
            step = 1
            curr = orders[x]
            if curr[1] == 0:
                x += step
                continue
            if curr[2] == 0: # buy order
                if len(sq) == 0 or sq[0].p > curr[0]:
                    heapq.heappush(bq, Order(curr[0], curr[1], curr[2]))
                else:
                    if curr[1] >= sq[0].a:
                        curr[1] -= sq[0].a
                        heapq.heappop(sq)
                        step = 0
                    elif curr[1] < sq[0].a:
                        sq[0].a -= curr[1]
            else: # sell order
                if len(bq) == 0 or bq[0].p < curr[0]:
                    heapq.heappush(sq, Order(curr[0], curr[1], curr[2]))
                else:
                    if curr[1] >= bq[0].a:
                        curr[1] -= bq[0].a
                        heapq.heappop(bq)
                        step = 0
                    elif curr[1] < bq[0].a:
                        bq[0].a -= curr[1]
            x += step
        ans = 0
        for x in bq:
            ans += x.a
        for x in sq:
            ans += x.a
        return ans%(10**9 + 7)