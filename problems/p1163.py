class Solution:
    def lastSubstring(self, s: str) -> str:
        return max(s[i:]for i in range(len(s)))


if __name__ == '__main__':
    assert Solution().lastSubstring("cacacb") == 'cb'