# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class RemoveSortedListDuplicates(object):
    def delete_duplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        cur = head
        nex = cur.next
        while nex != None:
            while nex.val == cur.val:
                if nex.next == None:
                    cur.next = None
                    return head
                nex = nex.next
            cur.next = nex
            cur = cur.next
            nex = nex.next
        return head
    

# From LeetCode: cleaner and faster, change cur.next every time,
# should be slow, but maybe fast due to less assignments
#
# class Solution(object):
#     def delete_duplicates(self, head):
#         cur = head
#         while cur:
#             while cur.next and cur.val == cur.next.val:
#                 cur.next = cur.next.next
#             cur = cur.next
#         return head


rsld = RemoveSortedListDuplicates()
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
res = rsld.delete_duplicates(head)
while res != None:
    print(res.val)
    res = res.next
