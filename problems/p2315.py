class Solution:
    def countAsterisks(self, line: str) -> int:
        words:list[str] = line.split('|')
        return sum(words[i].count('*') for i in range(len(words)) if i%2==0)