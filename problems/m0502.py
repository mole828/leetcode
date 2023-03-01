class Solution:
    def printBin(self, num: float) -> str:
        i = 0
        s = 'ERROR'
        while i < 31:
            num *= 2
            i += 1
            if num % 1 == 0:
                s = bin(int(num))[2 :]
                return '0.' + '0' * (i - len(s)) + s
        return s