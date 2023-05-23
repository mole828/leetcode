import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = []
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
