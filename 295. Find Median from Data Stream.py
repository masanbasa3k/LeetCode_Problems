
class MedianFinder:

    def __init__(self):
        self.bot, self.top = [], []
        
    def addNum(self, num: int) -> None:
        heappush(self.bot, -num)
        heappush(self.top, -heappop(self.bot))
        
        if len(self.top) > len(self.bot):
            heappush(self.bot, -heappop(self.top))
        
    def findMedian(self) -> float:
        if len(self.bot) != len(self.top):
            return -self.bot[0]
        else:
            return (self.top[0] - self.bot[0]) / 2
            
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()