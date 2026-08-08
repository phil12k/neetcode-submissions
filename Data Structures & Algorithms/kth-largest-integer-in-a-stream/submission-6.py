class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.k=k
        self.heap = nums
        heapq.heapify(self.heap)
        while self.k<len(self.heap):
            heapq.heappop(self.heap)



    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        while self.k<len(self.heap):
            heapq.heappop(self.heap)
        return self.heap[0]