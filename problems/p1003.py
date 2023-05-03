class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 3:
            return False
        t = []
        for c in s:
            t.append(c)
            if ''.join(t[-3:]) == 'abc':
                t[-3:] = []
        return not t
    
if __name__ == '__main__':
    assert Solution().isValid(s = "aabcbc")
    assert Solution().isValid(s = "abcabcababcc")
    assert not Solution().isValid(s = "abccba")
