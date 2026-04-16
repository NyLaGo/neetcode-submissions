class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+" : lambda a, b: a + b,
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: int(a/b)
        }
        stack = []

        for i in tokens:
            if i in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[i](a,b))
            else:
                stack.append(int(i))
        return stack[0]