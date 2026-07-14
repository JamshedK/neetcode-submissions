class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashset = ('*', '/', "+", '-')
        stack = []
        for token in tokens:
            if token not in hashset:
                stack.append(int(token))
                continue
            a = stack.pop()
            b = stack.pop()
            if token == '*':
                res = a * b 
                stack.append(res)
            elif token == '+':
                res = a + b
                stack.append(res)
            elif token == '-':
                res = b - a
                stack.append(res)
            else:
                res = int(b / a)
                stack.append(res)
        return stack[-1]