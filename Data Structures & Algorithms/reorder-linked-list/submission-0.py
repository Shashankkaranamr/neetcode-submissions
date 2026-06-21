# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Finding the middle element
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        head2=slow.next
        slow.next=None
    
        #Reversing the second part
        curr=head2
        prev=None
        nxt=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        head2=prev

        #Stiching the elements back
        itr1=head
        itr2=head2
        while itr2:
            temp1=itr1.next
            temp2=itr2.next
            itr1.next=itr2
            itr2.next=temp1

            itr1=temp1
            itr2=temp2
          
        



        


        

        