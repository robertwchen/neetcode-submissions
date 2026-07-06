class Solution:

    def encode(self, strs: List[str]) -> str:
        # turn ["mary ", "sue",] -> "4#mary3#sue"
        res_str = ""
        delim = '#'
        
        for s in strs:
            l = len(s)
            encoded_s = str(l) + delim + s
            res_str += (encoded_s)
        return res_str
             

    def decode(self, s: str) -> List[str]:
        # take in a "4#mary3#sue" -> return ["mary ", "sue"]
        decoded_str = []
        delim = '#' 
        i = 0
        current_num = 0
        
        
        while i < len(s):
            # if see number then go through number and save number and number index
            if s[i].isdigit():
                n_str = ""
                while s[i] != '#':
                    n_str += s[i]
                    i += 1
                n = int(n_str)
                i += 1

                # define string
                curr_s = s[i: i + n]
                print(f"current_s:{curr_s}")
                # curr_str = count from indices get string 
                decoded_str.append(curr_s)
                i = i + n
                print(i)
            else:
                break
        return decoded_str
            
