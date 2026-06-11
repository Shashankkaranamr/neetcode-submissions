class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash={}
        s2_hash={}
        left=0
        right=0
        if len(s2)<len(s1):
            return False
        for s in s1:
            s1_hash[s]=s1_hash.get(s,0)+1
        for right in range(len(s2)):
            s2_hash[s2[right]]=s2_hash.get(s2[right],0)+1
            
            if right-left+1>len(s1):
                if s2_hash[s2[left]]>1:
                    s2_hash[s2[left]]-=1
                else:
                    del s2_hash[s2[left]]
                left+=1
            if s1_hash==s2_hash:
                return True
        return False
    
        