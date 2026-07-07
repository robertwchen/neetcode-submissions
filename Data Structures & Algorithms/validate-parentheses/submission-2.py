class Solution:
    def isValid(self, s: str) -> bool:
        # map all values
        stack = []
        parantheses = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in parantheses:
                stack.append(c)
                
            else: #closed bracket
                if not stack:
                    return False
                open_bracket = stack[-1]
                print(open_bracket)
                if parantheses[open_bracket] == c:
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        return True
        