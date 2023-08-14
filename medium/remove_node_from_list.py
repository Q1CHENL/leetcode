# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class NodeRemover(object):
    def remove_nth_from_end(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        current = head
        nodes_dict = {}
        length = 0
        while current:
            nodes_dict[length] = current
            current = current.next
            length += 1
        if n == length:
            return head.next
        if n == 1:
            nodes_dict[length - 2].next = None
            return head  
        index = length - n
        nodes_dict[index - 1].next = nodes_dict[index + 1]
        return head


nodes = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
nodes1 = ListNode(1, None)
nodes = NodeRemover().remove_nth_from_end(nodes, 2)
print(nodes.val)
print(nodes.next.val)
print(nodes.next.next.val)
print(nodes.next.next.next.val)
