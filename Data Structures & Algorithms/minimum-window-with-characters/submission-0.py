class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_hash={}
        t_hash={}
        window=[-1,-1]
        have=0
        min_length=float("infinity")
        left=0
        

        for char in t:
            t_hash[char]=t_hash.get(char,0)+1
        need=len(t_hash)
        for right in range(len(s)):
            s_hash[s[right]]=s_hash.get(s[right],0)+1

            if s[right] in t_hash and t_hash[s[right]]==s_hash[s[right]]:
                have+=1
            while have==need:
                if right-left+1<min_length:
                    window=[left,right]
                    min_length=right-left+1
                s_hash[s[left]]-=1
                if s[left] in t_hash and t_hash[s[left]]>s_hash[s[left]]:
                    have-=1
                left+=1
        l,r=window
        return s[l:r+1] if min_length!=float("infinity") else ""
                
            