class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        left=0
        count = Counter(s1)
        for right in range(len(s2)):
            if right-left+1 == n:
                c1 = Counter(s2[left:right+1])
                if c1==count:
                    return True
                left+=1
        return False