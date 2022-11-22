class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        l = a * b
        s = sorted(list(set([x*a for x in range(b)]+[x*b for x in range(a)])))
        return (l * (n//len(s)) + s[n%len(s)]) % (10**9+7)

if __name__ == '__main__':
    print(Solution().nthMagicalNumber(3,8,9))
