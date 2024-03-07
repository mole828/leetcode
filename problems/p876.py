from tools.ListNode import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zero = ListNode(0, head) 
        a,b = zero,zero
        count = 0
        while b:
            b = b.next 
            count += 1
            if count == 2:
                a = a.next
                count = 0
        if count:
            a = a.next
        return a
        