class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        res=[]
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        def backtrack(curr_str,i):
            if i==len(digits):
                res.append(curr_str)
                return
            curr_arr=phone_map[digits[i]]
            for j in range(len(curr_arr)):
                backtrack(curr_str+curr_arr[j],i+1)
        backtrack("",0)
        return res
    