class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in ")}]":
                if not stack:
                    return False
                if p==')' and stack[-1]=='(':
                    stack.pop()
                elif p=='}' and stack[-1]=='{':
                    stack.pop()
                elif p==']' and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return not stack