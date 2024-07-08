class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        sweepLine = [0]*n
        for start, end, seats in bookings:
            start = start - 1
            sweepLine[start]+=seats
            if end < n:
                sweepLine[end]-=seats
        
        pfxsum = [0]*n
        pfxsum[0] = sweepLine[0]
        for i in range(1 , n):
            pfxsum[i] = pfxsum[i-1] + sweepLine[i]
        return pfxsum