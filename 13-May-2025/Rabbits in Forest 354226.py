# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        #intuition: we can group x+1 rabbits into the same group that
        #say answer x rabbits like me

        count = Counter(answers)
        res = 0
        for ans, cnt in count.items():
            group_size = ans+1
            no_of_groups = ceil(cnt/group_size)
            res += no_of_groups * group_size
        return res
