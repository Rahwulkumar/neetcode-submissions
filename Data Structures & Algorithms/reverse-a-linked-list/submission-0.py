# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        if head is None:
            return None
        
        current = head
        
        while current:
            stack.append(current.val)
            current = current.next
        
        current = head

        while current:
            current.val = stack.pop()
            current = current.next
        return head
        
        
        
        