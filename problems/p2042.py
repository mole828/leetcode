class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last = 0
        for word in s.split():
            if word.isnumeric():
                n = int(word)
                if n <= last : return False
                last = n
        return True