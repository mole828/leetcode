from typing import List
import re

def search (s: str):
    for i in range(len(s)):
        ss = s[:i] + ('.' if i!=0 else '') + s[i:]
        if re.match( r'^([1-9]\d*|0)(\.\d*[1-9])?$', ss ):
            yield ss
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]
        ans = []
        for i in range(1, len(s)):
            a, b = s[:i], s[i:]
            ans += [f'({x}, {y})' for x in search(a) for y in search(b)]
        return ans
                        

    

if __name__ == '__main__':
    sol = Solution()
    print(sol.ambiguousCoordinates("(123)"))