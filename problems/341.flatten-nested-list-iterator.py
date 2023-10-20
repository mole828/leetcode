#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

# @lc code=start
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
from typing import Iterable


class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> Iterable['NestedInteger']:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    __index: int
    __value: list[int]
    def __init__(self, nestedList: list['NestedInteger']):
        self.__value = []
        while nestedList:
            n = nestedList.pop(0)
            if n.isInteger():
                self.__value.append(n.getInteger())
            else:
                for i,nn in enumerate(n.getList()):
                    nestedList.insert(i,nn)
            # print(self.__value, nestedList)
        self.__index = 0
    
    def next(self) -> int:
        i = self.__index 
        self.__index += 1
        return self.__value[i]
    
    def hasNext(self) -> bool:
        return self.__index != len(self.__value)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

