class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        n = len(p)
        count = Counter(p)
        mp = defaultdict(int)
        left = 0
        for right in range(len(s)):
            mp[s[right]]+=1
            if right - left +1 == n:
                if mp == count:
                    ans.append(left)
                mp[s[left]] -= 1
                if mp[s[left]] == 0:
                    del mp[s[left]]
                left+=1
        return ans