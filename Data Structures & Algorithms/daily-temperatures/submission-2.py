class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonically decreasing stack 
        last_index = len(temperatures) - 1
        stack = [[temperatures[-1], 0]]
        res = [0] * (last_index + 1)
        for i, temp in enumerate(temperatures[::-1]):
            if i == 0: 
                continue
            # print(f"{stack}, curr {temp}")
            # check if stack is less than top
            while stack and temp >= stack[-1][0]:
                stack.pop()
            # if stack is empty, just append
            if not stack:
                stack.append([temp, i])
            # otherwise, set res[index] = stack[-1][1]
            else: 
                res[i] = i - stack[-1][1]
                stack.append([temp, i])
        return res[::-1]