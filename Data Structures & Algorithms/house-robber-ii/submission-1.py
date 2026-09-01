class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        order1=nums[1:]
        order2=nums[:len(nums)-1]
        a1,b1=0,0
        for c1 in order1:
            temp1=a1
            a1=max(c1+b1,a1)
            b1=temp1
        a2,b2=0,0
        for c2 in order2:
            temp2=a2
            a2=max(c2+b2,a2)
            b2=temp2
        return max(a1,a2)
            