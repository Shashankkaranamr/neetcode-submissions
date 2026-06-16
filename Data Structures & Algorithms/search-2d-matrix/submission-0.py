class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        high=len(matrix)-1
        mid=low+(high-low)//2
        while low<=high:
            if matrix[mid][0]==target:
                return True
            else:
                if matrix[mid][0]<target:
                    low=mid+1
                else:
                    high=mid-1
                mid=low+(high-low)//2
        row_low=0
        row_high=len(matrix[0])-1
        row_mid=row_low+(row_high-row_low)//2
        while row_low<=row_high:
            if matrix[high][row_mid]==target:
                return True
            else:
                if matrix[high][row_mid]<target:
                    row_low=row_mid+1
                else:
                    row_high=row_mid-1
                row_mid=row_low+(row_high-row_low)//2
        return False
        