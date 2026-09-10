class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = [0] * n
        temp = [[position[i], speed[i]] for i in range(len(position))]
        # sort temp by position
        temp.sort(key=lambda item: item[0], reverse=True)
        # print(temp)
        for i in range(len(position)):
            # calculate time needed
            pos, speed = temp[i][0], temp[i][1]
            time =((target - pos)/speed)
            stack[n - 1 - i] = time
        res = 0
        while stack: 
            # pop the top
            top = stack.pop()
            # keeping popping if top of stack is smaller or equal to top
            while stack and top >= stack[-1]:
                stack.pop()
            res += 1

        # basically identify how many unique ones
        return res