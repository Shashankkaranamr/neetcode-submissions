class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums={}
        arr=[]
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff not in hash_nums:
                hash_nums[nums[i]]=i
            else:
                arr.append(hash_nums[diff])
                arr.append(i)
        return arr
