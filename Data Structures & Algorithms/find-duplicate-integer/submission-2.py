class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Slow: what is the brute force?
            # loop through all numbers put it set
        #Repeat: what repeated work makes brute force slow?
            # checking each element
        #Store: what do I keep so I do not repeat work?
            # so instead of using a set you can use array itself as built in set and the index of the # as the set checker
        #Move: exactly when do pointers move / stack pop / heap push-pop?
            # when one element has been checked, mark its corresponding index number negative
        #Answer: when do I update result?
            # when encounter negative
        #Test: quick edge case + time/space.

        n = len(nums)  # how many numbers in array + 1


        # [ 1, 1, 2]
        for i, num in enumerate(nums):

            index = abs(num) - 1
            if nums[index] < 0:
                return index + 1
            
            nums[index] *= -1

        return



        