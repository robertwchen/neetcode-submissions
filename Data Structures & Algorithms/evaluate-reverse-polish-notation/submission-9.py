class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # define nums, make it a set
        stack = []
        
        for c in tokens:
            print(stack)
            if c == "+" or c == "-" or c == "*" or c == "/":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(self.perform_operation(val1, val2, c))

            else: 
                stack.append(int(c))
        return stack[0]

    def perform_operation(self, n1, n2, operator):
        if operator == "+":
            return n1 + n2
        elif operator == "-":
            return n1 - n2
        elif operator == "*":
            return n1 * n2
        elif operator == "/":
            return int(n1 / n2)