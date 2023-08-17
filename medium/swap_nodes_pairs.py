# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class PairsSwapper(object):
    def swap_pairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        prev = head
        prev_pair = prev  # connection between 2 pairs
        curr = head.next
        head = curr
        while True:
            tmp = curr.next
            curr.next = prev
            prev.next = tmp if tmp != None else None
            if prev.next == None or prev.next.next == None:
                return head
            curr = prev.next.next
            prev = prev.next
            prev_pair.next = curr
            prev_pair = prev

    # Sample from leetcode: recursion
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def recurse(node):
            if node == None:
                return None
            elif node.next == None:
                return node
            pointer = node
            temp = pointer.next
            pointer.next = recurse(temp.next)
            temp.next = pointer
            return temp
        return recurse(head)


l1_head = ListNode()
l1 = l1_head
for i in range(2, 10000):
    l1.next = ListNode(i, None)
    l1 = l1.next
list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
res = PairsSwapper().swap_pairs(l1_head)

# while res != None:
#     print(res.val)
#     res = res.next
