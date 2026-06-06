class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict=defaultdict()
        t_dict=defaultdict()
        for i in s:
            s_dict[i]=s_dict.get(i,0)+1
        for j in t:
            t_dict[j]=t_dict.get(j,0)+1
        if s_dict==t_dict:
            return True
        return False
        
        