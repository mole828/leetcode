from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        idx = logs[0][0]
        mx = logs[0][1]
        for i in range(1, len(logs)):
            t = logs[i][1] - logs[i - 1][1]
            if t >= mx:
                if t == mx:
                    idx = min(idx, logs[i][0])
                else:
                    idx = logs[i][0]
                mx = t
        return idx