class Solution:

    def encode(self, strs: List[str]) -> str:
        # string = num delim str
        encoded_str = ""
        for s in strs:
            encoded_str += (f"{len(s)}#{s}")
        return encoded_str


        #    5#Hello5#World
    def decode(self, s: str) -> List[str]:
        decoded = []
        ptr = 0
        while ptr < len(s):
            num = ""
            while s[ptr].isdigit():
                num += s[ptr]
                ptr += 1
            print(num)
            num = int(num)
            ptr += 1 # skip the #

            # from ptr -> ptr + num: convert
            word = s[ptr:ptr + num]
            decoded.append(word)
            ptr = ptr + num
            
        return decoded


s = ["Hello","World"]
sol = Solution()
print(sol.encode(s))