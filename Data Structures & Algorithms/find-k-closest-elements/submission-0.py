class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # arr = [2,4,5,8] x = 6 k = 2
        #       [4, 5, 8]
        
        # so first basically start on the center p1 p2 window
        # open window each direction taking the minium value difference from target val 
        
        p1 = 0
        p2 = len(arr) - 1
        
        while p2 - p1 + 1 > k:
            difA = abs(x - arr[p1])
            difB = abs(x - arr[p2])

            if difA <= difB:
                p2 -= 1
            else:
                p1 += 1
        return arr[p1:p2 + 1]