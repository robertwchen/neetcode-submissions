from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # place in counter count freq
        freq = Counter(nums)

        sorted_nums = sorted(freq.items(), key=lambda pair:pair[1] )

        result = []
        for num, count in sorted_nums[-k:]:
            result.append(num)
        return result

            

        # use sorted with lambda to get back value and reverse flag
        # return top k sorted
        