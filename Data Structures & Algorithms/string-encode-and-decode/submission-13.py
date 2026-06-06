class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=''
        for i in strs:
            j=len(i)
            encoded+=str(j)+"#"+i
        return encoded


    def decode(self, s: str) -> List[str]:
        List_str=[]
        def string_decode(s):
            if s=='':
                return 
            length=0
            for i in range(len(s)):
                if s[i]=='#':
                    break
                else:
                    length=length*10+int(s[i])
            List_str.append(s[i+1:i+length+1])
            
            string_decode(s[i+length+1:])
        string_decode(s)


        return List_str
