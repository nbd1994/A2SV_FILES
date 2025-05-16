# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

#leetcode editorial code
class Solution(object):
    # method to check if a part of the string is within the range 0-255,
    # returns True if part is within range 0-255 else False
    def valid(self, s, start, length):
        return length == 1 or (
            s[start] != "0"
            and (length < 3 or s[start : start + length] <= "255")
        )

    # main helper method to solve the problem by backtracking
    def helper(self, s, startIndex, dots, ans):
        remainingLength = len(s) - startIndex
        remainingNumberOfIntegers = 4 - len(dots)
        if (
            remainingLength > remainingNumberOfIntegers * 3
            or remainingLength < remainingNumberOfIntegers
        ):
            return
        if len(dots) == 3:
            if self.valid(s, startIndex, remainingLength):
                temp = ""
                last = 0
                for dot in dots:
                    temp += s[last : last + dot] + "."
                    last += dot
                temp += s[startIndex:]
                ans.append(temp)
            return
        for curPos in range(1, min(4, remainingLength + 1)):
            dots.append(curPos)
            if self.valid(s, startIndex, curPos):
                self.helper(s, startIndex + curPos, dots, ans)
            dots.pop()

    # main method called by leetcode
    def restoreIpAddresses(self, s):
        answer = []
        self.helper(s, 0, [], answer)
        return answer