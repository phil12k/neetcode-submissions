class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []
        

    def addNum(self, num: int) -> None:

        heapq.heappush(self.small, -num)
        #every element in small < big
        if self.small and self.big and (-self.small[0]>self.big[0]):
            small = heapq.heappop(self.small)
            big = heapq.heappop(self.big)

            heapq.heappush(self.small, -big)
            heapq.heappush(self.big, -small)

        if len(self.small)>len(self.big)+1:
            return heapq.heappush(self.big, -heapq.heappop(self.small))
        elif len(self.big)>len(self.small):
            return heapq.heappush(self.small, -heapq.heappop(self.big))
        

    def findMedian(self) -> float:
        if len(self.small)>len(self.big):
            return - self.small[0]
        return (-self.small[0]+self.big[0])/2
        
        