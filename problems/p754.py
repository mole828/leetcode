class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        sum = 1
        i = 2
        while sum< target or (sum - target)%2!=0:
            sum += i
            i += 1
        return i-1
