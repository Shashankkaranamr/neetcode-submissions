class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        for n in nums:
            hash_map[n]=hash_map.get(n,0)+1
        buckets=[[] for _ in range(len(nums)+1)]
        for num,freq in hash_map.items():
            buckets[freq].append(num)
        res=[]
        for i in range(len(buckets)-1,0,-1):
            
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res
