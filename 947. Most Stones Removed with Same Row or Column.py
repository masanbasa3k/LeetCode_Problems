from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        def clean(x, y):
            for nx in xs[y]:
                if (nx, y) not in visited:
                    visited.add((nx, y))
                    clean(nx, y)
            for ny in ys[x]:
                if (x, ny) not in visited:
                    visited.add((x, ny))
                    clean(x, ny)
        count = 0
        visited = set()
        
        xs = collections.defaultdict(list)
        ys = collections.defaultdict(list)
        
        for x, y in stones:
            xs[y].append(x)
            ys[x].append(y)
        for x, y in stones:
            if (x, y) not in visited:
                visited.add((x, y))
                clean(x, y)
                count += 1
        return len(stones) - count