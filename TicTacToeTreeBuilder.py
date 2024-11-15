from TicTacToe import TicTacToe
from TicTacToTree import Leaf, Root
from setup import SPACE, Users, PLANNED_STEPS
from Table import Table


class TicTacToeTreeBuilder:

    def __init__(self):
        pass

    @staticmethod
    def __generate_opportunities(root: Root, point: str, steps: int):
        if steps <= 0 or type(root) is Leaf:
            return
        root_table = root.Table
        spaces = root_table.Count(SPACE)
        if spaces == 0:
            return
        if root.ChildNumber == 0:
            for i in range(spaces):
                space_x, space_y = root_table.FindIndex(SPACE, number=i)
                tmp_table = root_table.copy()
                tmp_table[space_x, space_y] = point

                check_game_end = TicTacToe.GameIsEnd(tmp_table)

                if spaces == 1 or check_game_end:
                    current_node = Leaf(tmp_table)
                else:
                    current_node = Root(tmp_table)
                root.appChild(current_node)

        for i in range(root.ChildNumber):
            TicTacToeTreeBuilder.__generate_opportunities(root.getChild(i), Users.switch(point), steps - 1)

    @staticmethod
    def generate(root: Root, point = Users.Player):
        TicTacToeTreeBuilder.__generate_opportunities(root, point, PLANNED_STEPS)
        return root