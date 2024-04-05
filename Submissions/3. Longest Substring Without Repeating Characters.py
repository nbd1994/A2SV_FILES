class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        count = 0
        ans = 0
        left=0
        for right in range(len(s)):
            mp[s[right]]+=1
            if mp[s[right]]==1:
                ans = max(ans, right-left+1)
            while mp[s[right]]!=1:
                mp[s[left]]-=1
                left+=1
        return ans