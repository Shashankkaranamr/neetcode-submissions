class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=""
        i=0
        for i in range(len(s)):
            j=i
            for j in range(len(s)):
                length=j-i+1
                if length>len(longest):
                    sub_string=s[i:j+1]
                    if sub_string==sub_string[::-1]:
                        longest=sub_string
        return longest