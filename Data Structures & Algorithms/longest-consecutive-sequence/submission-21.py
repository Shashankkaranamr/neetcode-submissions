class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr_values=[0]
        hash_nums={}
        for i,j in enumerate(nums):
            if j-1 not in nums:
                hash_nums[j]=[]
        for key in hash_nums:
            hyp_key=key
            while hyp_key in nums:
                hash_nums[key].append(hyp_key)
                hyp_key+=1
        for key in hash_nums:
            arr_values.append(len(hash_nums[key]))
        return max(arr_values)
        

                
        

        