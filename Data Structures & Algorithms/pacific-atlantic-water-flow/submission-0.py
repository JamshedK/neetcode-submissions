class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Goal: DFS from both pacific and atlantic rows
        # Step1: 
            # Take top row, do a DFS and store all visited in pacific
            # Take left row, do a DFS and store all visited in pacific
            # do the same for right and bottom rows, store in atlantic
            # If a number exists in both, than it can be transferred
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(row, col, visited): 
            visited.add((row, col))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in directions: 
                r, c = row + dr, col + dc
                # only travel if you can
                if (r < 0 or r == ROWS
                        or c < 0 or c == COLS
                        or (r, c) in visited
                        or heights[r][c] < heights[row][col]):
                    continue
                dfs(r, c, visited)

            
        # try top and bottom columns
        for i in range(COLS):
            # top column is pacific
            dfs(0, i, pacific)
            # bottom column is atlantic
            dfs(ROWS-1, i, atlantic)
        
        # try left and right columns
        for i in range(ROWS):
            # left column pacific
            dfs(i, 0, pacific)
            # right column is atlantic
            dfs(i, COLS-1, atlantic)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic: 
                    res.append([r, c])
        
        return res






        