class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        positions = list(range(n))
        
        for row_idx in range(m):
            for pos_idx in range(n):
                if positions[pos_idx] > -1:
                    if grid[row_idx][positions[pos_idx]] == -1:
                        
                        if positions[pos_idx] == 0 or grid[row_idx][positions[pos_idx] - 1] == 1:
                            positions[pos_idx] = -1
                        else:
                            positions[pos_idx] -= 1
                    else:
                        if positions[pos_idx] == n - 1 or grid[row_idx][positions[pos_idx] + 1] == -1:
                            positions[pos_idx] = -1
                        else:
                            positions[pos_idx] += 1
        return positions