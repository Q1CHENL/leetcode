# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeKLists(object):
    def merge_k_lists_mysol(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        merged = ListNode()
        merged_head = merged
        min_node = None
        lists = [x for x in lists if x is not None]
        while len(lists) > 0:
            j = 0 # index of None to delete
            min_node = lists[0]
            for i in range(len(lists)):
                if lists[i].val >= min_node.val:
                    continue
                min_node = lists[i]
                j = i
            merged.next = min_node
            merged = merged.next
            lists[j] = lists[j].next
            if lists[j] == None:
                del lists[j]
        return merged_head.next
    
    
    # From leetcode sample solution
    # Faster on leetcode, but mine is faster locally
    # def merge_k_lists(self, lists):

    #     """
    #     :type lists: List[ListNode]
    #     :rtype: ListNode
    #     """
    #     vals = []

    #     for l in lists:
    #         while l:
    #             vals.append(l.val)
    #             l = l.next
        
    #     vals.sort()

    #     p1 = dummy = ListNode()

    #     for val in vals:
    #         p1.next = ListNode(val)
    #         p1 = p1.next

    #     return dummy.next
    
    
l1_head = ListNode()
l1 = l1_head
for i in range(2, 100000):
    l1.next = ListNode(i, None)
    l1 = l1.next

l2_head = ListNode()
l2 = l2_head
for i in range(100, 100000):
    l2.next = ListNode(i, None)
    l2 = l2.next

l3_head = ListNode()
l3 = l3_head
for i in range(400, 100000):
    l3.next = ListNode(i, None)
    l3 = l3.next
lists = [l1_head, l2_head, l3_head]
res = MergeKLists().merge_k_lists_mysol(lists)
while res != None:
    print(res.val)
    res = res.next
