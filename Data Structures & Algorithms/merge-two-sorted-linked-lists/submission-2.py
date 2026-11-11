# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        l , r = list1, list2
        h = []
        while l != None and r != None:
            if l.val <= r.val :
                h.append(l)
                l = l.next
            else :
                h.append(r)
                r = r.next
        while r != None:
            h.append(r)
            r = r.next
        while l != None:
            h.append(l)
            l = l.next
        for i in range(len(h)-1):
            h[i].next = h[i+1]
        h[-1].next = None
        return h[0]
        