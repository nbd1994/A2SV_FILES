# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        tms = sorted(enumerate(times), key=lambda x: x[1][0])
        n = len(times)
        chairs = [i for i in range(n)]
        heap = []
        for idx, interval in tms:
            arrive, leave = interval
            while heap and heap[0][0] <= arrive:
                lev, chair_id = heappop(heap)
                heappush(chairs, chair_id)
            available_chair = heappop(chairs)
            heappush(heap, (leave, available_chair))

            if targetFriend == idx:
                return available_chair
        return 0