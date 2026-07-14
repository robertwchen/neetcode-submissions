class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Pattern:
        # What algorithm shape is this?
        # 2 pointer

        # State:
        # What does each variable/store object mean?
        # p1 stores current front char, p2 stores current back char

        # Invariant:
        # What must stay true?
        # p1 must stay < p2 if same or cross then stop checking

        # Progress:
        # What moves/changes every loop or recursive call?
        # p1 moves up p2 moves down 

        # Update:
        # When do I count/save/return answer?
            # if p1 != p2 early return false
            # if p1 == p2 return true

        # Return:
        # What type do I return: bool/int/list/node/None?
            # boolean 

        # start p1 at 0 and p2 at len(s) - 1
        
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            if not s[p1].isalnum():
                p1 += 1
                continue
            if not s[p2].isalnum():
                p2 -= 1
                continue

            if s[p1].lower() != s[p2].lower():
                return False
            
            p1 += 1
            p2 -= 1
        return True
            
            # if current char at p2 isnt alnum inrement continue
            # if s[p1].lower() != s[p2].lower()
                # return False

