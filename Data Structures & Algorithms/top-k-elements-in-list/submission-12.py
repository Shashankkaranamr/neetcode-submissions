class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort algorithm
        hash_map={}
        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1
        buckets=[[] for _ in range(len(nums)+1)]
        for num,freq in hash_map.items():
            buckets[freq].append(num)
        
        result=[]
        for i in range(len(nums),0,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result)==k:
                    return result
        return result



            