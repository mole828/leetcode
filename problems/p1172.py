from heapq import heappop, heappush


class DinnerPlates:

    def __init__(self, capacity: int):
        self.stk=[]
        self.c=capacity
        self.delpos=[]
        self.dpset=set()

    def push(self, val: int) -> None:
        while self.delpos:
            pos=heappop(self.delpos)
            if pos in self.dpset:
                self.dpset.remove(pos)
                self.stk[pos]=val
                return
        self.stk.append(val)

    def pop(self) -> int:
        while len(self.stk)-1 in self.dpset:
            self.dpset.remove(len(self.stk)-1)
            self.stk.pop()
        if not self.stk:
            return -1
        return self.stk.pop()
    def popAtStack(self, index: int) -> int:
        offset=index*self.c
        if offset>=len(self.stk):
            return -1
        pos=min(len(self.stk),offset+self.c-1)
        while pos>=offset and pos in self.dpset:
            pos-=1
        if pos<offset:
            return -1
        heappush(self.delpos,pos)
        self.dpset.add(pos)
        return self.stk[pos]