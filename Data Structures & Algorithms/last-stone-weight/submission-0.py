class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            largest = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            diff = largest - second
            if diff > 0:
                heapq.heappush(heap, -diff)
        return -heap[0] if heap else 0
        
