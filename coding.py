"""
Problem: Merge Two Sorted Linked Lists

This file contains two implementations:
1. Recursive approach (easy to understand)
2. Iterative approach (optimal, O(1) extra space)
"""
from typing import Optional
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)
class RecursiveSolution:
    def mergeTwoLists(self,list1: Optional[ListNode],list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
class IterativeSolution:
    def mergeTwoLists(self,list1: Optional[ListNode],list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
if __name__ == "__main__":
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    print("Recursive:")
    rec = RecursiveSolution().mergeTwoLists(l1, l2)
    print_linked_list(rec)
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    print("Iterative:")
    itr = IterativeSolution().mergeTwoLists(l1, l2)
    print_linked_list(itr)
