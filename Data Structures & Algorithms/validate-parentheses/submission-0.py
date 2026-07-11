class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', '}': '{', ']': '[' }
        stack = []
        for ch in s:
            # check if character in dictionary, pop top of stack and compare 
            if ch in dic and stack: 
                top = stack.pop()
                # return false if it's the incorrect
                if top != dic[ch]:
                    return False
            # if not in dictionary, then add to stack
            else:
                stack.append(ch)
        
        return len(stack) == 0
