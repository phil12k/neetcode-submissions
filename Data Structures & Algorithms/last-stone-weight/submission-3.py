class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [ -stone for stone in stones ]

        while len(stones)>1:
            heapq.heapify(stones)
            largest = -heapq.heappop(stones)     
            heapq.heapify(stones)
            secondLargest = -heapq.heappop(stones) 
            diff = largest - secondLargest
            if diff!=0:
                heapq.heappush(stones, -diff)

        if len(stones)==0:
            return 0
        return -stones[0]