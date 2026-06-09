class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        max_length=0
        mem_hash={}
        sum=0
        for right in range(len(s)):
            if s[right] in mem_hash:
                mem_hash[s[right]]+=1
                
            else:
                mem_hash[s[right]]=1
            
            while (right - left + 1) - max(mem_hash.values()) > k:
                mem_hash[s[left]] -= 1
                left += 1
                
            max_length=max(max_length,right-left+1)

        return max_length
        