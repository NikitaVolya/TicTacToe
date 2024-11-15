from setup import SPACE
from Table import Table

class TicTacToe:

    @staticmethod
    def CheckLines(table: Table) -> str:
        for i in range(3):
            if table[i, 0] != SPACE and\
                    table[i, 0] == table[i, 1] and\
                    table[i, 1] == table[i, 2]:
                return table[i, 0]
            if table[0, i] != SPACE and\
                    table[0, i] == table[1, i] and\
                    table[1, i] == table[2, i]:
                return table[0, i]
        return ""

    @staticmethod
    def CheckDiagonal(table: Table) -> str:
        if SPACE != table[0, 0] and\
                table[0, 0] == table[1, 1] and\
                table[1, 1] == table[2, 2]:
            return table[0, 0]
        if SPACE != table[0, 2] and\
                table[0, 2] == table[1, 1] and\
                table[1, 1] == table[2, 0]:
            return table[0, 2]
        return ""

    @staticmethod
    def GameIsEnd(table: Table) -> str:
        if winner := TicTacToe.CheckLines(table):
            return winner
        if winner := TicTacToe.CheckDiagonal(table):
            return winner
        return ""

    @staticmethod
    def allCellFull(table: Table) -> bool:
        for i in range(table.Height):
            for j in range(table.Width):
                if table[i, j] == SPACE:
                    return False
        return True

    @staticmethod
    def checkGame(table: Table) -> str | None:
        if winner := TicTacToe.GameIsEnd(table):
            return winner
        if TicTacToe.allCellFull(table):
            return "draw"
        return None