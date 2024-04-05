class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s=s.lower()
        # newString = [char for char in s if char.isalnum()]
        # return newString == newString[::-1]

        s = s.lower()
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True 
        
        