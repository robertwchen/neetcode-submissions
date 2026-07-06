class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # now use heapq
        # first use Counter to store freq
        freq = Counter(nums)
        heap = []

        for num, count in freq.items():
            heap.append((-count, num))

        heapq.heapify(heap)

        result = []

        for _ in range(0, k):
            count, num = heapq.heappop(heap)
            result.append(num)

        return result



        # now itemize and loop through

        # then turn the array into heap using heapify
        # then using heap for however many elements
            # pop those elments
            # add to result