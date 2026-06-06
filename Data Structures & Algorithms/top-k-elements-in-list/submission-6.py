class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_hash={}
        res=[]
        for i in nums:
            nums_hash[i]=nums_hash.get(i,0)+1
        for j in range(k):
            m=max(nums_hash, key=nums_hash.get)
            res.append(m)
            nums_hash[m]=0
        return res
        