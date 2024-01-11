class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        curr = head
        f = head
        temp = None
        while f:
            f = f.next
            curr.next = temp
            temp = curr
            curr = f
        return temp

        