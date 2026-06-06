class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,suffix=[],[]
        for i,j in enumerate(nums):
            if i==0:
                temp=1
            else:
                temp=temp*nums[i-1]
            prefix.append(temp)
        k=len(nums)-1
        while k>=0:
            if k==len(nums)-1:
                temp1=1
            else:
                temp1=temp1*nums[k+1]
            suffix.append(temp1)
            k=k-1
        out=[]
        for m,n in enumerate(nums):
            out.append(prefix[m]*suffix[len(nums)-m-1]) 
        return out
            
        
            
