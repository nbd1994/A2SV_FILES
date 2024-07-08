class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        d = collections.Counter()
        for l, r, right in shifts:
            d[l] +=1 if right else -1
            if r+1 < n:
                d[r+1] += -1 if right else 1
        pfx = [0]
        result = ""
        for i in range(n):
            cur = pfx[-1] + d[i]
            pfx.append(cur)
            result += string.ascii_lowercase[(ord(s[i]) - ord('a') + cur) % 26]
        return result