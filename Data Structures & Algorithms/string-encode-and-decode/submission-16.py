class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=''
        for i in strs:
            j=len(i)
            encoded_str+=str(j)+"#"+i
        return encoded_str
        


    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            start=j+1
            end=start+length
            result.append(s[start:end])
            i=end
       
        return result
            

       