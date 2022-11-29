
class Solution:
    def minOperations(self, s: str) -> int:
        cnt = sum(int(c) != i % 2 for i, c in enumerate(s))
        return min(cnt, len(s) - cnt)


if __name__ == '__main__':
    Solution().minOperations("0100")