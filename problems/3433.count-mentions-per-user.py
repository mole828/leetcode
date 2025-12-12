#
# @lc app=leetcode id=3433 lang=python3
#
# [3433] Count Mentions Per User
#

# @lc code=start
import enum
from typing import List

from sortedcontainers import SortedList


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:

        class EventType(enum.Enum):
            OFFLINE = (1, "OFFLINE")
            MESSAGE = (2, "MESSAGE")

            def __lt__(self, other):
                return self.value[0] < other.value[0]
            def __eq__(self, other):
                return self.value[0] == other.value[0]
            def __gt__(self, other):
                return self.value[0] > other.value[0]
            
        events: List[tuple[int, str, str]] = SortedList(
            (int(event_time_str), EventType[event_type_str], event_data_str)
            for event_type_str, event_time_str, event_data_str in events
        )
        now = 0
        up_time = [0] * numberOfUsers
        mentions = [0] * numberOfUsers
        while events:
            event_time, event_type, event_data_str = events.pop(0)
            now = event_time
            match event_type:
                case EventType.MESSAGE:
                    match event_data_str:
                        case "ALL":
                            for i in range(numberOfUsers):
                                mentions[i] += 1
                        case "HERE":
                            for i in range(numberOfUsers):
                                if up_time[i] <= now:
                                    mentions[i] += 1
                        case _:
                            event_data_str: str
                            user_id_list = [
                                int(user_id_str.replace("id", ""))
                                for user_id_str in 
                                event_data_str.split()
                            ]
                            for user_id in user_id_list:
                                mentions[user_id] += 1
                case EventType.OFFLINE:
                    user_id = int(event_data_str)
                    up_time[user_id] = now + 60
            print(mentions)
        return mentions
        
# @lc code=end

# print(Solution().countMentions(
#     2,
#     [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]
# ))

print(Solution().countMentions(
    3,
    [["MESSAGE","5","HERE"],["OFFLINE","10","0"],["MESSAGE","15","HERE"],["OFFLINE","18","2"],["MESSAGE","20","HERE"]]
))