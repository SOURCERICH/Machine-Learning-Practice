class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        current = self.head
        for i in range(index):
            if not current:
                return -1
            current = current.next
        return current.data if current else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
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
        new_node = Node(val)
        current = self.head
        for i in range(index - 1):
            if not current:
                return
            current = current.next
        if not current:
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
        for i in range(index - 1):
            if not current:
                return
            current = current.next
        if not current or not current.next:
            return
        current.next = current.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

linked_list = MyLinkedList()
linked_list.addAtHead(1)
linked_list.addAtTail(3)
linked_list.addAtIndex(1,2)
print(linked_list.get(1))  
linked_list.deleteAtIndex(1)
print(linked_list.get(1)) 
