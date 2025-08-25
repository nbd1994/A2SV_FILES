# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(sub='', index=0):
            if index == len(s):
                result.append(sub)
                return
            if s[index].isalpha():
                backtrack(sub + s[index].lower(), index + 1)
                backtrack(sub + s[index].upper(), index + 1)
            else:
                backtrack(sub + s[index], index + 1)

        backtrack()
        return result