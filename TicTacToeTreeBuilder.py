from DegugOutput import DebugOutput
from TicTacToe import TicTacToe
from TicTacToTree import Leaf, Root, Node
from setup import SPACE, Users, LEVELS

class TicTacToeTreeBuilder:

    @staticmethod
    def __create_node(root: Root, point: str, i: int, is_leaf: bool = False) -> None:
        table = root.Table.copy()
        space_x, space_y = table.FindIndex(SPACE, number=i)
        table[space_x, space_y] = point

        if is_leaf:
            node = Leaf(table)
        elif TicTacToe.GameIsEnd(table):
            node = Leaf(table)
        else:
            node = Root(table)

        same_child = root.findChild(table)
        if not same_child:
            root.appChild(node)
        else:
            same_child.Weight += 1


    @staticmethod
    def __generate_opportunities(root: Root, point: str, steps: int) -> None:
        if steps <= 0 or root.IsLeaf:
            return
        spaces = root.Table.Count(SPACE)
        if spaces == 0:
            return
        if root.ChildNumber == 0:
            for i in range(spaces):
                TicTacToeTreeBuilder.__create_node(root, point, i, spaces == 1)

        for i in range(root.ChildNumber):
            TicTacToeTreeBuilder.__generate_opportunities(root.getChild(i), Users.switch(point), steps - 1)

    @staticmethod
    def generate(root: Root, point = Users.First, steps=LEVELS["normal"]):
        DebugOutput.print("Start generate tree | steps:", steps)
        TicTacToeTreeBuilder.__generate_opportunities(root, point, steps)
        DebugOutput.print("Generate of tree is done! Root score: ", root.Score)
        return root