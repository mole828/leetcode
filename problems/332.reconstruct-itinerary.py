#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        itinerary = []
        def dfs(airport):
            print(airport, graph)
            while graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)
            print(itinerary)
        
        dfs("JFK")
        return itinerary[::-1]

# @lc code=end
assert Solution().findItinerary( 
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]] 
) == ["JFK","MUC","LHR","SFO","SJC"]

assert Solution().findItinerary( 
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
) == ["JFK","ATL","JFK","SFO","ATL","SFO"]

assert Solution().findItinerary( 
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
) == ["JFK","NRT","JFK","KUL"]