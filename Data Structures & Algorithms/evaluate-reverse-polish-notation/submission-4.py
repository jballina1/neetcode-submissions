class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+-*/"
        for i in range(len(tokens)):
            cur = tokens[i]
            if cur not in ops:
                stack.append(int(cur))
            elif cur in ops:
                num1 = stack.pop()
                num2 = stack.pop()
                if cur == "+":
                    stack.append(num1 + num2)
                elif cur == "-":
                    stack.append(num2 - num1)
                elif cur == "*":
                    stack.append(num1 * num2)
                elif cur == "/":
                    stack.append(int(float(num2) / num1))
        return stack[-1]
