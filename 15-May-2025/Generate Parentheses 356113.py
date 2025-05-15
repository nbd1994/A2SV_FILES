# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stk = []
        res = []
        def backtrack(openP, closeP):
            if openP == closeP == n:
                res.append("".join(stk))
                return
            if openP < n:
                stk.append('(')
                backtrack(openP+1, closeP)
                stk.pop()
            if closeP < openP:
                stk.append(')')
                backtrack(openP, closeP+1)
                stk.pop()
            
        backtrack(0,0)
        return res