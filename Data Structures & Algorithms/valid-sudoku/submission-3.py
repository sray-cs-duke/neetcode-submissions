class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]       # Set for each row
        cols = [set() for _ in range(9)]       # Set for each column
        boxes = [set() for _ in range(9)]      # Set for each box
        for r in range(9):                     # Visit every row
            for c in range(9):                 # Visit every column
                number = board[r][c]           # Current character
                if number == ".":              # Ignore empty cells
                    continue
                box = (r // 3) * 3 + (c // 3)  # Find box index
                if (
                    number in rows[r] or       # Duplicate in row
                    number in cols[c] or       # Duplicate in column
                    number in boxes[box]       # Duplicate in box
                ):
                    return False               # Sudoku is invalid
                rows[r].add(number)             # Record in row
                cols[c].add(number)             # Record in column
                boxes[box].add(number)          # Record in box
        return True                             # No duplicates found