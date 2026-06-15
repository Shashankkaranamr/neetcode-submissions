class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
         left=0
         right=0
         area_arr=[]
         for h in range(len(heights)):
            left=h
            right=h
            while left!=0:
                    
                if heights[left-1]<heights[h]:
                    break
                left-=1
            while right!=len(heights)-1:
                if heights[right+1]<heights[h]:
                    break
                right+=1
            area_arr.append(heights[h]*(right-left+1))
         return max(area_arr)
            

       
                
            

       
    
    
            

        