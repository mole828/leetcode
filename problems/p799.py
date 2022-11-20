class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for y in range(1, query_row+1):
            next_row = [0]*(y+1)
            for j, volume in enumerate(row):
                if volume > 1:
                    next_row[j] += (volume - 1) / 2
                    next_row[j + 1] += (volume - 1) / 2
            row = next_row
            
        return min(1, row[query_glass])
