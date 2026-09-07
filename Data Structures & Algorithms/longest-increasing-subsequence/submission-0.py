class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LOA=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i,len(nums)):
                if nums[i]<nums[j]:
                    LOA[i]=max(LOA[i],1+LOA[j])
        return max(LOA)