class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        arr = sorted([a,b,c])
        s2 = sum(arr)/2
        if arr[-1] > s2:return arr[0]+arr[1]
        return int(s2)