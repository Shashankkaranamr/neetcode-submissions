class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        def checker(s,l,r):
            if l>=r:
                return True
            if not s[l].isalnum():
                l+=1
                return checker(s,l,r)
            if not s[r].isalnum():
                r-=1
                return checker(s,l,r)
            else:
                if s[r].lower()!=s[l].lower():
                    return False
                r-=1
                l+=1
                return checker(s,l,r)
        return checker(s,left,right)

        
        


        