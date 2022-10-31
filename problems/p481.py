class Solution:
    def magicalString(self, n: int) -> int:
        index = 2
        string = '122'
        while len(string) < n:
            string += int(string[index]) * '1'
            index+=1
            string += int(string[index]) * '2'
            index+=1
        return string.count('1', 0, n)