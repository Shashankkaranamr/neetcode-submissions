from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output_array=[]
        max_queue=deque()

        for right in range(len(nums)):

            if max_queue and max_queue[0]<right-k+1:
                max_queue.popleft()
            while max_queue and nums[max_queue[-1]]<nums[right]:
                max_queue.pop()
            max_queue.append(right)

            if right>=k-1:
                output_array.append(nums[max_queue[0]])

        return output_array
            


            
        
        