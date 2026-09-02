class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result=max(nums)
        curr_max,curr_min=1,1

        for n in nums:
            if n!=0:
                temp=curr_max*n
                curr_max=max(n,n*curr_max,n*curr_min)
                curr_min=min(n,temp,n*curr_min)
                result=max(result,curr_max)
            else:
                curr_max,curr_min=1,1
        return result


        