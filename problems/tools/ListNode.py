from typing import Optional


class ListNode:
    val: int 
    next: Optional['ListNode']
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}->{self.next}"

    def build(arr: list[int]) -> Optional['ListNode']:
        if arr:
            head = ListNode(val=arr.pop(0))
            node = head 
            while arr:
                node.next = ListNode(val=arr.pop(0))
                node = node.next 
            return head 
        
        