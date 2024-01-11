
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def build_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

class Solution:
    def detectCycle(self, head: [ListNode]) -> [ListNode]:
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                s = head
                while s != f:
                    s = s.next
                    f = f.next
                return s
        return None


input_values = [3, 2, 0, -4]
linked_list = build_linked_list(input_values)

linked_list.next.next.next.next = linked_list.next

solution = Solution()
cycle_start = solution.detectCycle(linked_list)

if cycle_start:
    print("Cycle detected. Starting node value:", cycle_start.val)
else:
    print("No cycle detected.")
