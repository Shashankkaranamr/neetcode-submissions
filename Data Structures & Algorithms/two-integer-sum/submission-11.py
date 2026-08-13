class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for n in range(len(nums)):
            if nums[n] in hash_map:
                return [hash_map[nums[n]],n]
            else:
                hash_map[target-nums[n]]=n
        return -1