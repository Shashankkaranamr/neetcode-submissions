class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_hash={}
        left=0
        right=0
        max_length=0
        for right in range(len(s)):
            s_hash[s[right]]=s_hash.get(s[right],0)+1
            while (right-left+1)-max(s_hash.values())>k:
                s_hash[s[left]]-=1
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length
            
        