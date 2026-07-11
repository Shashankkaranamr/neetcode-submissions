class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtrack(subset_str,count_open,count_closed):
            if len(subset_str)==2*n:
                result.append(subset_str)
                return
            if count_open<n:
                backtrack(subset_str+"(",count_open+1,count_closed)
            if count_closed<count_open:
                backtrack(subset_str+")",count_open,count_closed+1)

        backtrack("",0,0)
        return result
        