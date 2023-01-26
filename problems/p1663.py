class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        zn = (k-n)//25
        mid = (k-n)%25
        return 'a'*(n-1-zn)+chr(ord('a')+mid)+'z'*zn if n > zn else 'z'*n