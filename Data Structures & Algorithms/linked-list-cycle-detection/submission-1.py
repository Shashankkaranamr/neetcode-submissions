# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        itr=head
        hash_map={}
        if head:
            while itr.next:
                if itr.next in hash_map:
                    return True
                else:
                    hash_map[itr]=1
                itr=itr.next
        return False
            


        