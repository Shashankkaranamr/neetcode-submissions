class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_mem={}
        left=0
        right=0
        max_length=0
        while right!=len(s):
            if s[right] in char_mem and char_mem[s[right]]>=left:
                
                left=char_mem[s[right]]+1
            
            else:
                char_mem[s[right]]=right
                right+=1
                max_length=max(max_length,right-left)

        return max_length
        

            
        