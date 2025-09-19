#
# @lc app=leetcode id=3484 lang=python3
#
# [3484] Design Spreadsheet
#

# @lc code=start
class Spreadsheet:

    def __init__(self, rows: int):
        self.data = [
            [
                0 for _ in range(rows)
            ] for _ in range(26)
        ]

    def place(cell: str) -> tuple[int, int]:
        r = ord(cell[0]) - ord('A')
        c = int(cell[1:]) - 1
        return r, c
    
    def getCell(self, cell: str) -> int:
        r,c = Spreadsheet.place(cell)
        return self.data[r][c]

    def setCell(self, cell: str, value: int) -> None:
        r,c = Spreadsheet.place(cell)
        self.data[r][c] = value

    def resetCell(self, cell: str) -> None:
        r,c = Spreadsheet.place(cell)
        self.data[r][c] = 0

    def getValue(self, formula: str) -> int:
        _, expr = formula.split('=')
        a, b = expr.split('+')
        va = int(a) if a.isdigit() else self.getCell(a)
        vb = int(b) if b.isdigit() else self.getCell(b)
        return va + vb


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
# @lc code=end