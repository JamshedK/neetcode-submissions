class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Goal: backtracking, we pass two numbers, num_open, num_closed
        # base case: if num_open == num_closed == n, we stop add paranthesis and move one
        # recursive case: 
            # if num_open == num_closed, we can only add open
            # elif num_open == n, we can only add closed
            # otherwise, we can add both open and closed
        res = []
        def dfs(curr, num_open, num_closed):
            if num_open == num_closed == n: 
                res.append(curr)
                print(curr)
                return 
            elif num_open == num_closed: 
                dfs(curr + '(', num_open + 1, num_closed)
            elif num_open == n:
                dfs(curr + ')', num_open, num_closed + 1)
            else: 
                dfs(curr + '(', num_open + 1, num_closed)
                dfs(curr + ')', num_open, num_closed + 1)
        
        dfs('', 0, 0)
        return res

