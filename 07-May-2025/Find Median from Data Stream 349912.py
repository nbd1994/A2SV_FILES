# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []
    def addNum(self, num: int) -> None:
        heappush(self.small, -num)

        if self.small and self.large and (-self.small[0] > self.large[0]):
            num = - heappop(self.small)
            heappush(self.large, num)
        if len(self.small) > len(self.large) + 1:
            num = - heappop(self.small)
            heappush(self.large, num)
        if len(self.large) > len(self.small) + 1:
            num = heappop(self.large)
            heappush(self.small, -num)
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return - self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()