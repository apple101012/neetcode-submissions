from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        square = defaultdict(list)
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                sq = (r // 3, c // 3)
                if value in row[r] or value in col[c] or value in square[sq]:
                    return False
                row[r].append(value)
                col[c].append(value)
                square[sq].append(value)
        return True
