# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
    
    def hasCycle(self, head: [ListNode]) -> bool:
        slowPointer = self.head
        fastPointer = self.head
        
        while (slowPointer != None and fastPointer != None and fastPointer.next != None):
            slowPointer.next
            fastPointer.next.next
        if (slowPointer == fastPointer):
            return True
        return False
        
        
            
        