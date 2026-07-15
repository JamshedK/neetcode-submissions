class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            # if temperature is small, keep adding 
            if not stack or temp < stack[-1][0]:
                stack.append([temp, i])
            # otherwise, decreasing monotonic stack is requirement is not met
            else: 
                while stack and stack[-1][0] < temp:
                    top_temp, top_index = stack[-1] 
                    # update res array
                    res[top_index] = i - top_index 
                    # pop the top elemenet
                    stack.pop()
                # add the curr temperature
                stack.append([temp, i])
        
        return res