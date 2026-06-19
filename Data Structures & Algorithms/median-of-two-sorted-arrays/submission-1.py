class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1>nums2:
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        low=0
        high=m
        half=(m+n+1)//2

        while low<=high:
            partition_a=low+(high-low)//2
            partition_b=half-partition_a

            left_a=float("-inf") if partition_a==0 else nums1[partition_a-1]
            right_a=float("inf") if partition_a==m else nums1[partition_a]
            left_b=float("-inf") if partition_b==0 else nums2[partition_b-1]
            right_b=float("inf") if partition_b==n else nums2[partition_b]

            if left_a<=right_b and left_b<=right_a:
                if (m+n)%2==0:
                    return((max(left_a,left_b)+min(right_a,right_b))/2.0)
                else:
                    return max(left_a,left_b)
            elif left_a>right_b:
                high=partition_a-1
            else:
                low=partition_a+1
           

        