# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        fast = slow = head
        prev = dummy

        for i in range(1, n):
            fast = fast.next
        
        while fast.next:
            prev = prev.next
            fast = fast.next
            slow = slow.next


        prev.next = slow.next

        return dummy.next