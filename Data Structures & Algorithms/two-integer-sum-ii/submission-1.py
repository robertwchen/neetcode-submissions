class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted increasing order
        # just point beginning and end if sum greater move left pointer if sum greater move right 
        # if found return [p1, p2]
        # return false

        p1 = 0
        p2 = len(numbers) - 1

        while p1 < p2:
            sum = numbers[p1] + numbers[p2]

            if sum == target:
                return [p1 + 1, p2 + 1]
            
            # while less than increment left pointer
            if sum < target:
                p1 += 1
            else:
                p2 -= 1

        return false


        