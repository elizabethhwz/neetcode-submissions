class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        Row = [set() for _ in range(rows)]
        Col = [set() for _ in range(cols)]
        Box = [[set() for _ in range(cols//3)] for _ in range(rows//3)]
        for r in range(rows):
            for c in range(cols):
                cell = board[r][c]
                if cell != "." and cell in Row[r]:
                    return False
                elif cell != "."  and cell in Col[c]:
                    return False
                elif cell != "." and cell in Box[r//3][c//3]:
                    return False
                else:
                    Row[r].add(cell)
                    Col[c].add(cell)
                    Box[r//3][c//3].add(cell)
        return True