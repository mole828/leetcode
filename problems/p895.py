from collections import Counter


class FreqStack:

    def __init__(self):
        self.data = Counter()
        self.freq = list()

    def push(self, val: int) -> None:
        self.data[val] += 1
        cnt = self.data[val]
        if cnt > len(self.freq):
            self.freq.append([val, ])
        else:
            self.freq[cnt - 1] .append(val)

    def pop(self) -> int:
        val = self.freq[-1].pop()
        self.data[val] -= 1
        if not self.freq[-1]:
            self.freq.pop()
        return val

if __name__ == '__main__':
    fs = FreqStack()
    fs.push(5)
    fs.push(7)
    fs.push(5)
    fs.push(7)
    fs.push(4)
    fs.push(5)
    fs.pop()
    fs.pop()
    fs.pop()
    fs.pop()

