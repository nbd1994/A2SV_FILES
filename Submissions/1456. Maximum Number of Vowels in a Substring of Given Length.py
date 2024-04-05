class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        count = 0
        ans = 0
        left=0
        for right in range(len(s)):
            if s[right] in vowels:
                count+=1
            while right-left+1 > k:
                if s[left] in vowels:
                    count-=1
                left+=1
            ans = max(ans, count)
        return ans