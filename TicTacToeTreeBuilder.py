from DegugOutput import DebugOutput
from TicTacToe import TicTacToe
from TicTacToTree import Leaf, Root, Node
from setup import SPACE, Users, LEVELS
from Table import Table


class TicTacToeTreeBuilder:

    def __init__(self):
        pass

    @staticmethod
    def __create_node(table: Table, point: str, i: int, is_leaf: bool = False) -> Node:
        space_x, space_y = table.FindIndex(SPACE, number=i)
        table[space_x, space_y] = point

        if is_leaf:
            return Leaf(table)
        if TicTacToe.GameIsEnd(table):
            return Leaf(table)
        return Root(table)

    @staticmethod
    def __generate_opportunities(root: Root, point: str, steps: int) -> None:
        if steps <= 0 or root.IsLeaf:
            return
        spaces = root.Table.Count(SPACE)
        if spaces == 0:
            return
        if root.ChildNumber == 0:
            for i in range(spaces):
                node = TicTacToeTreeBuilder.__create_node(root.Table.copy(), point, i, spaces == 1)
                root.appChild(node)

        for i in range(root.ChildNumber):
            TicTacToeTreeBuilder.__generate_opportunities(root.getChild(i), Users.switch(point), steps - 1)

    @staticmethod
    def generate(root: Root, point = Users.First, steps=LEVELS["normal"]):
        DebugOutput.print("Start generate tree | steps:", steps)
        TicTacToeTreeBuilder.__generate_opportunities(root, point, steps)
        return root