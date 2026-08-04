class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            stoneOne = heapq.heappop(maxHeap)
            stoneTwo = heapq.heappop(maxHeap)
            if stoneOne != stoneTwo:
                heapq.heappush(maxHeap, stoneOne - stoneTwo)

        return -maxHeap[0] if maxHeap else 0