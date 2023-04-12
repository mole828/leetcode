class Solution:
    def longestDecomposition(self, text: str) -> int:
        length = 1
        begin = 0
        ans = 0
        while begin + length <= len(text)/2:
            left = text[begin:begin+length]
            right = text[-(begin+length):len(text)-begin]
            print(left, right)
            length += 1
            if left == right:
                length, begin = 1, length+begin-1
                ans += 2
        print(begin, length, len(text))
        if begin != len(text)/2:
            ans += 1
        return ans

if __name__ == '__main__':
    print(Solution().longestDecomposition(text = "elvtoelvto"))