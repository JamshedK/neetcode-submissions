class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Loop through the matrix, every position becomes a starting point
        # for every position, do a DFS
        # base case: 
            # if curr pos (x, y) outside of matrix, exit
            # if all characters in word have been processed, return True
            # if curr pos (x, y) does not equal current ch, skip and return 
        # recursive case:
            # if curr pos (x, y) does equal current ch, update to the next character 
            # loop through possible moving positions (top, bottom, left, right), and pass those

        def dfs(r, c, i):
            if i >= len(word):
                return True
            elif (r < 0 or r >= len(board) 
                    or c < 0 or c >= len(board[0]) 
                    or (r, c) in seen):
                return False
            elif board[r][c] != word[i]:
                return False
            seen.add((r, c))
            # recursive case
            res = (dfs(r -1, c, i + 1) 
                or dfs(r + 1, c, i + 1)
                or dfs(r, c - 1, i + 1)
                or dfs(r, c + 1, i + 1) )
            seen.remove((r, c))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                seen = set()
                if dfs(i, j, 0) == True: 
                    return True

        return False

