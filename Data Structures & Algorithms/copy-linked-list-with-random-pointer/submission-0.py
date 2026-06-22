"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        itr1=head
        reference_hash={}
        while itr1:
            reference_hash[itr1]=Node(itr1.val)
            itr1=itr1.next

        itr1=head
       
        
        while itr1:
            itr2=reference_hash[itr1]
            itr2.next=reference_hash.get(itr1.next)
            itr2.random=reference_hash.get(itr1.random)
            itr1=itr1.next

        return reference_hash[head]



            


            
