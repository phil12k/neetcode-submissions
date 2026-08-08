class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [ -stone for stone in stones ]
        heapq.heapify(stones)

        while len(stones)>1:
            largest = -heapq.heappop(stones)    
            secondLargest = -heapq.heappop(stones) 
            diff = largest - secondLargest
            if diff!=0:
                heapq.heappush(stones, -diff)

        if len(stones)==0:
            return 0
        return -stones[0]