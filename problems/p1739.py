class Solution:
    def minimumBoxes(self, n: int) -> int:
        num, i, j = 0, 0, 0
        while num < n:
            i += 1
            num += (i * (i + 1)) // 2
        num -= (i * (i + 1)) // 2
        while num < n: 
            j += 1
            num += j
        return (i * (i - 1)) // 2 + j 