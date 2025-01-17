
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: [ListNode], val: int) -> [ListNode]:
        prev, curr = None, head
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                curr = curr.next
            else:
                prev, curr = curr, curr.next
        return head
        