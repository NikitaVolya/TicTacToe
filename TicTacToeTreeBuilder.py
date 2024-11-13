from TicTacToe import TicTacToe
from TicTacToTree import Leaf, Root
from setup import SPACE, Users, copy_table


class TicTacToeTreeBuilder:

    def __init__(self):
        pass

    @staticmethod
    def __get_spaces(table: list[list[str]]) -> int:
        rep: int = 0
        for row in table:
            for cell in row:
                if cell == SPACE:
                    rep += 1
        return rep

    @staticmethod
    def __get_clear_celle(table: list[list[str]], index: int) -> (int, int):
        for i in range(3):
            for j in range(3):
                if table[i][j] == SPACE:
                    if index == 0:
                        return i, j
                    else:
                        index -= 1
        return -1, -1

    @staticmethod
    def __generate_node(root: Root, table: list[list[str]], point: str):

        spaces = TicTacToeTreeBuilder.__get_spaces(table)

        if spaces == 0:
            return

        for i in range(spaces):
            space_x, space_y = TicTacToeTreeBuilder.__get_clear_celle(table, i)
            tmp_table = copy_table(table)
            tmp_table[space_x][space_y] = point
            check_game_end = TicTacToe.GameIsEnd(tmp_table)

            if spaces == 1 or check_game_end:
                current_node = Leaf(tmp_table)
            else:
                current_node = Root(tmp_table)
                TicTacToeTreeBuilder.__generate_node(current_node, tmp_table, Users.switch(point))

            root.appChild(current_node)

    @staticmethod
    def generate(table: list[list[str]], point = Users.Player):
        assert len(table) == 3
        assert len(table[0]) == len(table[1]) == len(table[2]) == 3
        root = Root(table)
        TicTacToeTreeBuilder.__generate_node(root, table, point)
        return root