
class Users:
    Player: str = "X"
    AI: str = "O"

    @staticmethod
    def switch(point: str):
        if point == Users.Player:
            return Users.AI
        if point == Users.AI:
            return Users.Player
        return None

SPACE = " "

def copy_table(table: list[list[str]]) -> list[list[str]]:
    rep = []
    for i in range(len(table)):
        rep.append(table[i].copy())
    return rep

def table_comparison(table1: list[list[str]], table2: list[list[str]]) -> bool:
    for i in range(3):
        for j in range(3):
            if table1[i][j] != table2[i][j]:
                return False
    return True

def print_table(table):
    for row in table:
        print("|", end=" ")
        for symbl in row:
            print(symbl, end=" ")
        print("|")
    print()
