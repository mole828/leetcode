#
# @lc app=leetcode id=2402 lang=python3
#
# [2402] Meeting Rooms III
#

# @lc code=start
from collections import defaultdict
from typing import List

from sortedcontainers import SortedList

# Time Limit Exceeded, 71 / 82 testcases passed
class Solution:
    def mostBooked(self, n: int, meetings: List[tuple[int,int]]) -> int:
        meetings.sort()
        events: defaultdict[int, list[int]] = defaultdict(list)
        rooms_count = [0] * n
        rooms = [True] * n
        now = 0
        while meetings:
            if events[now]:
                for i in events[now]:
                    rooms[i] = True
            while meetings and meetings[0][0] <= now:
                meeting = meetings.pop(0)
                start, end = meeting
                spend = end - start
                if any(rooms): # 如果到会议时间 且 如果有空余房间
                    for i in range(n): 
                        if rooms[i]: # 找到空余房间
                            rooms[i] = False # 修改房间为不可用
                            events[now+spend].append(i) 
                            rooms_count[i] += 1
                            break
                else: 
                    meetings.insert(0, meeting)
                    break 
            # print({
            #     'now':now, 
            #     'rooms': rooms, 
            #     'meetings': meetings
            #     # 'events': events,
            # })
            now += 1
            
        # print(rooms_count)
        return rooms_count.index(max(rooms_count))


class Solution:
    def mostBooked(self, n: int, meetings: List[tuple[int,int]]) -> int:
        meetings.sort()
        rooms: List[List[tuple[int,int]]] = [[]for _ in range(n)]
        while meetings:
            start, end = meetings.pop(0)
            spend = end - start 
            room_ends = [room[-1][-1] if room else 0 for room in rooms]
            room_waits = [max(room_end-start,0) for room_end in room_ends]
            room_belong = room_waits.index(min(room_waits))
            wait = room_waits[room_belong]
            rooms[room_belong].append((start+wait,end+wait))
            # print({
            #     'start': start,
            #     'end': end,
            #     'spend': spend,
            #     'room_ends': room_ends,
            #     'room_waits': room_waits,
            #     'room_belong': room_belong,
            # })
        room_used = [len(room) for room in rooms]
        return room_used.index(max(room_used))
            
    
# @lc code=end

print(Solution().mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]))
print(Solution().mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]))