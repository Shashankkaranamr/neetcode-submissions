class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=defaultdict(list)

        for n in nums:
            a[n]=a.get(n,0)+1
        
        for n in a:
            if a[n]!=1:
                return True
        return False
           

        