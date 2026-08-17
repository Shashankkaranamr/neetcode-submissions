class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal=[]
        number_set=set(["1","2","3","4","5","6","7","8","9","0"])
        for char in s:
            if ord(char.lower())>96 and ord(char.lower())<96+26:
                pal.append(char.lower())
            if char in number_set:
                pal.append(char.lower())

            
        print(pal)
        return True if pal[::-1]==pal else False
        
        


        