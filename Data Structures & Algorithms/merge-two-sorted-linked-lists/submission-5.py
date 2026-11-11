# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        h = []
        while list1 and list2 :
            if list1.val <= list2.val :
                h.append(list1)
                list1 = list1.next
            else :
                h.append(list2)
                list2 = list2.next
        while list1 :
            h.append(list1)
            list1 = list1.next
        while list2 :
            h.append(list2)
            list2 = list2.next
        for i in range(len(h)-1):
            h[i].next = h[i+1]
        h[-1].next = None
        return h[0]
        