class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(index,pos,rem):
            if rem==0:
                result.append(pos[:])
                return
            if rem<0 or index==len(nums):
                return
            pos.append(nums[index])
            backtrack(index,pos,rem-nums[index])
            pos.pop()

            backtrack(index+1,pos,rem)
        backtrack(0,[],target)
        return result