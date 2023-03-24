from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = ""
        self.words = words

    def query(self, letter: str) -> bool:
        self.s += letter
        return any(self.s.endswith(x) for x in self.words)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)