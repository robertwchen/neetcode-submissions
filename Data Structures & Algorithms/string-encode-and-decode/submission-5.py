# where am I
    # at some point on the string
# what am I doing
# what do I return


class Solution:
# turn ["a", "bb"] into 1#a2#bb
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            s_len = str(len(s))
            encoded.append(s_len + '#' + s)
        encoded_s = ""
        for segment in encoded:
            encoded_s += segment
        return encoded_s

    5#Hello5#World
    def decode(self, s: str) -> List[str]:
        # loop through chars 
        decoded = []
        ptr = 0
        print(len(s))
        while ptr < len(s):
            print("hello")
            num_s = ""
            while s[ptr] != '#':
                num_s += s[ptr]
                ptr += 1

            ptr += 1 #skip 
            num = int(num_s)
            word = ""
            for i in range(num):
                word += s[ptr]
                ptr += 1
            decoded.append(word)
        return decoded



