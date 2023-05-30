class MyHashSet:
    _set: set
    def __init__(self):
        self._set = set()

    def add(self, key: int) -> None:
        self._set.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self._set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self._set


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)