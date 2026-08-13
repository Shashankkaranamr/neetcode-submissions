class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hash={}
        for i in nums:
            if i in nums_hash:
                return True
            else:
                nums_hash[i]=nums_hash.get(i,0)+1
        return False