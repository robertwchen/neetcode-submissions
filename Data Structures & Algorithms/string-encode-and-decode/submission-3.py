class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode with # plus delim
        result = ""
        for s in strs:
            # check how long
            str_length = len(s)
            s_segment = str(str_length) + '#' + s
            result += s_segment
        print(result)
        return(result)


    # 5#Hello5#World
    
    def decode(self, s: str) -> List[str]:
        p = 0
        result = []
        while p < len(s):
            length_str = ""
            while s[p] is not '#':
                length_str += s[p]
                print(s[p], p, length_str)
                p += 1  

            p += 1 
            
            length = int(length_str)
            word = s[p:p + length]
            p += length
            result.append(word)
        return result
            # take that many c's and move pointer to after
