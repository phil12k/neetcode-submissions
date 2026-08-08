class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones)>1:
            l1 = -heapq.heappop(stones)
            l2 = -heapq.heappop(stones)
            diff =abs(l1-l2)
            if diff>0:
                heapq.heappush(stones,-diff)
            
        return -stones[0] if stones else 0