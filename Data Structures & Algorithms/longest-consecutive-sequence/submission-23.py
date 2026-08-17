class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length=0
        num_set=set(nums)
        for n in num_set:
            length=1
            if n-1 not in num_set:
                while n+1 in num_set:
                    length+=1
                    n+=1
            max_length=max(max_length,length)
        return max_length
       

                
        

        