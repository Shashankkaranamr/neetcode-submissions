# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head=ListNode(0,head)
        node_before_sublist=dummy_head

        while True:
            sublist_end=self.get_sublist_end(node_before_sublist,k)

            if not sublist_end:
                break
            
            start=node_before_sublist.next
            node_after_sublist=sublist_end.next
            prev=node_after_sublist
            curr=start
            while curr!=node_after_sublist:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            node_before_sublist.next=sublist_end
            node_before_sublist=start
        return dummy_head.next

    def get_sublist_end(self,node,k):
        while node and k>0:
            node=node.next
            k-=1
        return node





        