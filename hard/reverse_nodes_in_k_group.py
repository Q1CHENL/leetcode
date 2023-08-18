# Given the head of a linked list, reverse the nodes of the list k at a time,
# and return the modified list.

# k is a positive integer and is less than or equal to the length of the
# linked list. If the number of nodes is not a multiple of k then left-out
# nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may
# be changed.

# Simply put: reverse every k nodes

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class KGroupReverser(object):
    # My solution: find all k sublists and then link them all together
    def reverse_k_group(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head
        
        # depends
        # total_len = self.length(head)
        # if k > total_len:
        #     k = total_len

        sl = self.sub_lists(k, head)
        reversed_sl = []
        for t in sl[:-1]:
            reversed_sl.append(self.reverse_list(t[0]))
        
        # handle last sublist: reverse or not
        reversed_sl.append((sl[-1][0], sl[-1][1]) if self.length(sl[-1]
                           [0]) < k else self.reverse_list(sl[-1][0]))

        final_head = reversed_sl[0][0]
        for i in range(len(reversed_sl) - 1):
            reversed_sl[i][1].next = reversed_sl[i+1][0]
        return final_head

    def sub_lists(self, k, head):
        lists = []
        next_head = head
        while True:
            knodes = self.find_next_k(k, next_head)
            if knodes[1] == None:
                lists.append(knodes)
            # No need, already handled in reverse_k_group
            # or (knodes[0] == knodes[1] and knodes[2] == None):
                return lists
            next_head = knodes[2]

    # find next k nodes in the given head
    def find_next_k(self, k, head):
        tmp = head
        for i in range(k - 1):
            if tmp != None:
                tmp = tmp.next
                continue
            return (head, None, None)
        ret = (head, tmp, tmp.next if tmp != None else None)
        if tmp != None:
            tmp.next = None
        return ret

    # reverse a linked list
    def reverse_list(self, head):
        if head == None:
            return (None, None)
        if head.next == None:
            return (head, None)
        prev = head
        curr = head.next
        head.next = None
        while curr != None:
            tmp = ListNode(curr.val, curr.next)
            curr.next = prev
            prev = curr
            curr = tmp.next
        return (prev, head)

    def print_list(self, head):
        while head != None:
            print(head.val)
            head = head.next

    def length(self, head):
        len = 0
        while head != None:
            len += 1
            head = head.next
        return len


list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

reverser = KGroupReverser()

l1_head = ListNode()
l1 = l1_head
for i in range(1, 10):
    l1.next = ListNode(i, None)
    l1 = l1.next

for i in range(11):
    l1_head = ListNode()
    l1 = l1_head
    for j in range(1, 10):
        l1.next = ListNode(j, None)
        l1 = l1.next
    reverser.print_list(reverser.reverse_k_group(l1_head, i))
    print(f"\n{i}\n")
