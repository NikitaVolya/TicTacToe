from setup import SPACE

class TicTacToe:

    @staticmethod
    def CheckLines(table: list[list]) -> str:
        for i in range(3):
            if table[i][0] == table[i][1] and table[i][1] == table[i][2] and table[i][0] != SPACE:
                return table[i][0]
            if table[0][i] == table[1][i] and table[1][i] == table[2][i] and table[0][i] != SPACE:
                return table[0][i]
        return ""

    @staticmethod
    def CheckDiagonal(table: list[list]) -> str:
        if SPACE != table[0][0] == table[1][1] == table[2][2]:
            return table[0][0]
        if SPACE != table[0][2] == table[1][1] == table[2][0]:
            return table[0][2]
        return ""

    @staticmethod
    def GameIsEnd(table: list[list]) -> str:
        if winner := TicTacToe.CheckLines(table):
            return winner
        if winner := TicTacToe.CheckDiagonal(table):
            return winner
        return ""

    @staticmethod
    def allCellFull(table: list[list]) -> bool:
        for row in table:
            for cell in row:
                if cell == SPACE:
                    return False
        return True

    @staticmethod
    def checkGame(table: list[list]) -> str | None:
        if winner := TicTacToe.GameIsEnd(table):
            return winner
        if TicTacToe.allCellFull(table):
            return "draw"
        return None