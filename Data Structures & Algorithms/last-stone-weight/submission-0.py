class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap, -s)
        while len(maxHeap) > 0:
            stoneOne = heapq.heappop(maxHeap) * -1
            if len(maxHeap) == 0:
                return stoneOne
            stoneTwo = heapq.heappop(maxHeap) * -1
            diff = stoneOne - stoneTwo
            if diff != 0:
                heapq.heappush(maxHeap, -diff)
        return 0
