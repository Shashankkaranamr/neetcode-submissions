class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for s in strs:
            i=len(s)
            encoded_string+=str(i)+"#"+s
        print(encoded_string)
        return encoded_string
        


    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            result.append(s[j+1:j+length+1])
            i=length+j+1
        return result



        
       