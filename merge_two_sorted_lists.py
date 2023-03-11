from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeTwoSortedLists:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        merged = ListNode()
        merged_head = merged
        cursor_1, cursor_2 = list1, list2
        prev = None
        while cursor_1 != None or cursor_2 != None:
            if cursor_2 == None or (cursor_1 != None and cursor_1.val <= cursor_2.val):
                merged.val = cursor_1.val
                cursor_1 = cursor_1.next
            else:
                merged.val = cursor_2.val
                cursor_2 = cursor_2.next
            prev = merged
            merged.next = ListNode()
            merged = merged.next
        # set merged to None only deletes the reference 'merged',
        # becasue the element is still refed by merged_head so it
        # won't be set to null
        prev.next = None
        return merged_head


m = MergeTwoSortedLists()
l1 = ListNode(1, ListNode(2, ListNode(4, None)))
l2 = ListNode(1, ListNode(3, ListNode(4, None)))

l3 = m.merge_two_lists(l1, l2)
print(f'{l3.val}')
l3 = l3.next
print(f'{l3.val}')
l3 = l3.next
print(f'{l3.val}')
l3 = l3.next
print(f'{l3.val}')
l3 = l3.next
print(f'{l3.val}')
l3 = l3.next
print(f'{l3.val}')
