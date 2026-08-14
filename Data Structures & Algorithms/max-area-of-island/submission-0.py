from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            visited.add((r, c))
            q = deque([(r, c)])
            area = 1
            while q: 
                r, c = q.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions: 
                    new_row, new_col = r + dr, c + dc
                    if (new_row in range(rows) 
                            and new_col in range(cols)
                            and (new_row, new_col) not in visited 
                            and grid[new_row][new_col] == 1):
                        area += 1
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
            return area
        visited = set()
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited: 
                    area = bfs(r, c)
                    print(area)
                    max_area = max(max_area, area)

        return max_area