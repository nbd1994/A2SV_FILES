class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mp = zip(heights, names)
        answer = sorted(mp,  reverse = True)

        return [name for height, name in answer]