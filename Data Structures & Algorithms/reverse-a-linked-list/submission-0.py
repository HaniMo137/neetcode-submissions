# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :
            return head
        l = [head]
        while head.next != None :
            head = head.next
            l.append(head)
        for k in range(1,len(l)):
            l[-k].next = l[-k-1]
        l[0].next = None
        return l[-1]
        
        
