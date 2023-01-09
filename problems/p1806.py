class Solution:
    def reinitializePermutation(self, n: int) -> int:
        x = n // 2
        ans = 1
        while x != 1:
            if x % 2:
                x = (x + n - 1) // 2
            else:
                x = x // 2
            ans += 1
        return ans