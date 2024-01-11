class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        s,f = head, head
        while n:
            f = f.next
            n -= 1
        if not f:
            return head.next
        while f.next:
            s = s.next
            f = f.next
        s.next = s.next.next
        return head



        