class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0":
            return 0
        prev1= 1 if int(s[-1])!=0 else 0
        prev2=1
        n=len(s)
        count=0

        for i in range(n-2,-1,-1):
            current=0
            if s[i]!="0":
                current=prev1
                if 10<=int(s[i:i+2])<=26 :
                    current+=prev2
            prev2=prev1
            prev1=current
        return prev1