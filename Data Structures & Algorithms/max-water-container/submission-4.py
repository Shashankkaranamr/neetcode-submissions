class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front=0
        end=len(heights)-1
        
        def calculate_volume(front,end):
            return (end-front)*min(heights[front],heights[end])
        max_volume=(calculate_volume(front,end))
        while front!=end:
            if heights[front]>heights[end]:
                end-=1
            else:
                front+=1
            max_volume=max(max_volume,calculate_volume(front,end))

        return max_volume
        