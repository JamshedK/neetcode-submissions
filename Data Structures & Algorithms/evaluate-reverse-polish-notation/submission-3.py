class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        hashset = set(['*', '+', '-', '/'])
        stack = []
        for token in tokens:
            if token not in hashset:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                res = eval(f"{a} {token} {b}")
                res = int(res)
                stack.append(res)
        return stack[-1]

