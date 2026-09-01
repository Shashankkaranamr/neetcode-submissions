class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b=0,0
        for loot in reversed(nums):
            temp=a
            a=max(loot+b,a)
            b=temp

        return a
        