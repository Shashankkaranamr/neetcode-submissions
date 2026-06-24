# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l1=None
        l2=None
        for i in range(len(lists)):
            l2=lists[i]
            l1=self.mergeTwolists(l1,l2)
        return l1

    def mergeTwolists(self,l1,l2):
        dummy=ListNode()
        itr=dummy

        while l1 or l2:
            value1=l1.val if l1 else float("inf")
            value2=l2.val if l2 else float("inf")
            if value1>=value2:
                itr.next=l2
                l2=l2.next
            else:
                itr.next=l1
                l1=l1.next
            itr=itr.next
        return dummy.next
        