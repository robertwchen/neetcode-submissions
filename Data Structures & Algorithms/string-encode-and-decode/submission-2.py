class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += (f"{len(s)}#{s}")
        return result
        # idea is to encode str to len # str

    def decode(self, s: str) -> List[str]:
        # idea is to turn 4#stri to stri, 
        result = []
        i = 0
        while i < len(s):
            num_str = ""

            while s[i] != '#':
                num_str += s[i]
                i += 1

            length = int(num_str)
            i += 1     
        
            result.append(s[i: i + length])
            i += length

        return result

strs = ["Hello","World"] 
#strs2 = [""] 
#sol = Solution()
#print(sol.encode(strs))
#print(sol.encode(strs2))
