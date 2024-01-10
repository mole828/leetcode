#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start

from collections import defaultdict

# XXX: 可以改
class Trie:
    data: dict[str, 'Trie']
    words: set[str]
    def __init__(self):
        self.data = defaultdict(Trie)
        self.words = set()


    def insert(self, word: str) -> None:
        self.words.add(word)
        if word:
            self.data[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        return word in self.words
        if word:
            first = word[0]
            if first not in self.data:
                return False
            return self.data[first].search(word[1:])
        return True

    def startsWith(self, prefix: str) -> bool:
        if prefix:
            first = prefix[0]
            if first not in self.data:
                return False
            return self.data[first].startsWith(prefix[1:])
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

