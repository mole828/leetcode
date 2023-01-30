# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        nodeA = list1
        for _ in range(a-1):nodeA=nodeA.next
        nodeB = nodeA
        for _ in range(b-a+2):nodeB=nodeB.next
        list2last = list2
        while list2last.next!=None:list2last=list2last.next
        nodeA.next = list2
        list2last.next = nodeB
        return list1
