class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        for _ in range(index):
            if current is None:
                return -1
            current = current.next
        if current is None:
            return -1 
        return current.val
    
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.head)
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return
        new_node = ListNode(val)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                return 
            current = current.next
        if current is None:
            return
        new_node.next = current.next
        current.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                return 
            current = current.next
        if current is None or current.next is None:
            return
        current.next = current.next.next

    def printLinkedList(self) -> None:
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList()
linked_list.addAtHead(1)
linked_list.addAtTail(3)
linked_list.addAtIndex(1, 2)
print(linked_list.get(1)) 
linked_list.deleteAtIndex(1) 
print(linked_list.get(1)) 
linked_list.printLinkedList()