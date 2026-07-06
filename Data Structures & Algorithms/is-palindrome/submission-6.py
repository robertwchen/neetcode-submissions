class Solution:
    def isPalindrome(self, s: str) -> bool:
        # basically 2 pointer
        s_list = list(s)
        p1 = 0
        p2 = len(s) - 1
        # start beginning and end
        while p1 < p2:
            while p1 < p2 and not s_list[p1].isalnum():
                p1 += 1
            while p1 < p2 and not s_list[p2].isalnum():
                p2 -= 1
 
            s_list[p1] = s_list[p1].lower()
            s_list[p2] = s_list[p2].lower()
            
            print(s_list[p1], s_list[p2])
            if s_list[p1] != s_list[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True

        