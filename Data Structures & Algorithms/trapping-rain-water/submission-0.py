class Solution:
    def trap(self, height: List[int]) -> int:
        arr_left=[]
        arr_right=[0]*len(height)
        min_arr=[]
        total=0
        max_left=0
        max_right=0
        for i in height:
            if i>max_left:
                max_left=i
            arr_left.append(max_left)
        for j in range(len(height)-1,-1,-1):
            if height[j]>max_right:
                max_right=height[j]
            arr_right[j]=max_right
        for k in range(len(height)):
            if arr_left[k]<arr_right[k]:
                min_arr.append(arr_left[k])
            else:
                min_arr.append(arr_right[k])
        for m in range(len(height)):
            if min_arr[m]-height[m]>0:
                total+=min_arr[m]-height[m]
        return total




        