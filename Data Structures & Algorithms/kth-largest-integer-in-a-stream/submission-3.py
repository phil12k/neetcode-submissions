class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.stream = nums
        self.k = k
        heapq.heapify(self.stream)
        while self.k< len(self.stream):
            heapq.heappop(self.stream)

      
        

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        if self.k<len(self.stream):
            heapq.heappop(self.stream)
            
        return self.stream[0]

      