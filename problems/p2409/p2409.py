from itertools import accumulate

DAYS = list(accumulate([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], initial = 0))

def day2int(s: str) -> int:
    m, d = map(int, s.split('-'))
    return d + DAYS[m - 1]

class Solution:
    def countDaysTogether(self, aa: str, la: str, ab: str, lb: str) -> int:
        ans = min(day2int(la), day2int(lb)) - max(day2int(aa), day2int(ab)) + 1
        return ans if ans > 0 else 0