class Solution:
    def alphabetBoardPath(self, target: str) -> str:

        res = []
        pre, x, y = 'a', 0, 0

        for ch in target:
            if ch == pre:
                res.append('!')
                continue

            idx = ord(ch) - ord('a')
            nx, ny = idx // 5, idx % 5

            if nx < x:
                res.append('U' * (x - nx))
            if ny < y:
                res.append('L' * (y - ny))

            if nx > x:
                res.append('D' * (nx - x))
            if ny > y:
                res.append('R' * (ny - y))

            res.append('!')
            pre, x, y = ch, nx, ny

        return ''.join(res)