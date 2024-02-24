#
# @lc app=leetcode id=2092 lang=python3
#
# [2092] Find All People With Secret
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


# Time Limit Exceeded, 37/55 cases passed
class Solution:
    def findAllPeople(self, n: int, meetings: List[tuple[int,int,int]], firstPerson: int) -> List[int]:
        # dict[time, list[meeting(a,b)]]
        events:dict[int, list[tuple[int,int]]] = defaultdict(list)
        for a,b,time in meetings:
            events[time].append((a,b))
        # print(events)
        knows = set([0,firstPerson])
        for time in sorted(time for time in events):
            # print(time)
            while True:
                last = knows.copy()
                for a,b in events[time]:
                    # print(a,b)
                    if a in knows:
                        knows.add(b)
                    if b in knows:
                        knows.add(a)
                if knows == last:
                    break 
        return knows
    

class Solution:
    def findAllPeople(self, n: int, meetings: List[tuple[int,int,int]], firstPerson: int) -> List[int]:
        known_set = set([0, firstPerson])
        
        sorted_meetings: list[list[tuple[int,int]]] = []
        meetings.sort(key=lambda x:x[-1])

        seen_time = set()
        
        for meeting in meetings:
            if meeting[-1] not in seen_time:
                seen_time.add(meeting[-1])
                sorted_meetings.append([])
            sorted_meetings[-1].append((meeting[0], meeting[1]))

        for meeting_group in sorted_meetings:
            people_know_secret = set()
            graph:dict[int, list[int]] = defaultdict(list)
            
            for p1, p2 in meeting_group:
                graph[p1].append(p2)
                graph[p2].append(p1)
                if p1 in known_set:
                    people_know_secret.add(p1)
                if p2 in known_set:
                    people_know_secret.add(p2)
                    
            queue:deque[int] = deque((people_know_secret))
        
            while queue:
                curr = queue.popleft()
                known_set.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in known_set:
                        known_set.add(neighbor)
                        queue.append(neighbor)

        return list(known_set)
# @lc code=end

print(Solution().findAllPeople(n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1))
