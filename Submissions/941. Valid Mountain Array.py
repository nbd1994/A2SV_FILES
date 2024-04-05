class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) == 1:
            return False
        increasing, previous = None, arr[0]
        for e in arr[1:]:
            if previous == e:
                return False
            if increasing is None:
                if e <= previous:
                    return False
                increasing = True
            elif increasing and previous > e:
                increasing = False
            elif not increasing and previous < e:
                return False
            previous = e

        return not increasing