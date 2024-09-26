#
# @lc app=leetcode id=729 lang=python3
# @lcpr version=
#
# [729] My Calendar I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

class MyCalendar:
    def __init__(self):
        self.booked = []

    def overlap(a,b,c,d: int) -> bool:
        return c < b and a < d

    def book(self, start: int, end: int) -> bool:
        if any(MyCalendar.overlap(start,end, l,r) for l, r in self.booked):
            return False
        self.booked.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end



