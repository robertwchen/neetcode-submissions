# where am I

# what am I doing
# what do I return

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        if len(nums) == 0:
            return []
        
        buckets = [[] for i in range(len(freq) + 2)]
        print(buckets)

        for n in freq:
            print(n)
            print(freq[n])
            buckets[freq[n]].append(n)
        
        result = []
        count = 0
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            for n in bucket:
                result.append(n)
                count += 1
                if count == k:
                    return result

        return []

    