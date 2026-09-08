class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target=sum(nums)//2
        dp=set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            next_set=set()
            for n in dp:
                if n+nums[i]==target:
                    return True
                next_set.add(n+nums[i])
                next_set.add(n)
            dp=next_set
        return False