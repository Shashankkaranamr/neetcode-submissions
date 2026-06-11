class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_hash={}
        left=0
        right=0
        max_length=0
        for right in range(len(s)):
           
            if s[right] in s_hash and s_hash[s[right]] >= left:
                left=s_hash[s[right]]+1
            s_hash[s[right]]=right
            max_length=max(max_length,right-left+1)
        return max_length
        