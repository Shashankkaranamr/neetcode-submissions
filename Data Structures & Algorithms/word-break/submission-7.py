class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        result=""
        result_arr=[""]


        for i in range(0,len(s),1):
            curr_char=s[i]
            #print(curr_char)
            result=False
            for j,p in enumerate(result_arr):
                
                #print(j)
                #print(p)
                new_char=result_arr[j]+curr_char
                result_arr[j]=new_char
                
                if new_char in wordDict:
                    result=True
            if result==True:result_arr.append("")
                    
        return result

            

        