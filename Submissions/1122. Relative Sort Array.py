class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = Counter(arr1)
        ans = []
        for num in arr2:
            while mp[num] > 0:
                ans.append(num)
                mp[num]-=1
            if mp[num]==0:
                del mp[num]
        for key in sorted(mp.keys()):
            while mp[key]> 0:
                ans.append(key)
                mp[key]-=1
        return ans
        
        