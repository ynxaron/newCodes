import heapq
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        # minHeap with k largest elements
        self.minHeap, self.k = nums, k
        # heapifying our nums array, making it such that
        # self.nums[0] is the smallest and self.nums[-1] is the largest
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            # as long as our self.minHeap is greater than k, keep removing (and readjusting, hence
            # we are using heapq.heappop() method) till we have a self.minHeap with length == self.k
            heapq.heappop(self.minHeap)

    def add(self, n: int) -> int:
        # pushing onto our self.minHeap
        heapq.heappush(self.minHeap, n)
        if len(self.minHeap) > self.k:
            # if we have our length after adding the new element is larger than self.k, then we pop (and readjust)
            heapq.heappop(self.minHeap)
        return self.minHeap[0] # returning the minimum value (which, in an array of k-most largest elements, would be the kth largest element)
