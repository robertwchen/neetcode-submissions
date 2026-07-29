class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        bucket = [[] for i in range(len(nums) + 1)]

        print(freq)
        for num, freq in freq.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]: # -> list
                result.append(num)
                k -= 1
                if k == 0:
                    return result
        return result
            
            