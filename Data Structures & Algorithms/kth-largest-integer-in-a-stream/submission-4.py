class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while self.k< len(self.heap):
            heapq.heappop(self.heap)

      
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if self.k<len(self.heap):
            heapq.heappop(self.heap)
            
        return self.heap[0]

      