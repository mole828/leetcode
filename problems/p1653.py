class Solution:
    def minimumDeletions(self, s: str) -> int:
        a,b = 0,0
        for ss in s:
            if ss == 'b':
                b += 1
            else:
                if b > 0:
                    b -= 1
                a += 1
        return len(s)-a-b