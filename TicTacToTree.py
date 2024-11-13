from TicTacToe import TicTacToe
from setup import Users, copy_table, table_comparison


class Node:

    def __init__(self, table: list[list[str]]):
        self.parent: Node | None = None
        self.table = copy_table(table)
        self.score = 0

    def CalculateScore(self):
        pass

    @property
    def Score(self) -> int:
        return self.score

    @property
    def IsLeaf(self) -> bool:
        return False


class Root(Node):

    def __init__(self, table: list[list[str]]):
        self.__children: [Node] = []
        super(Root, self).__init__(table)

    def CalculateScore(self):
        rep: int = 0
        for node in self.__children:
            rep += node.Score / 10
        self.score = rep

        if self.parent:
            self.parent.CalculateScore()

    def appChild(self, child: Node):
        self.__children.append(child)
        child.parent = self
        self.CalculateScore()

    def findChild(self, table: list[list]):
        for child in self.__children:
            if table_comparison(child.table, table):
                return child

    def getBestChild(self) -> Node | None:
        if not self.__children:
            return None
        index = 0
        max_score = self.__children[0].Score
        for i in range(1, len(self.__children)):
            tmp_score = self.__children[i].Score
            if tmp_score > max_score:
                index = i
                max_score = tmp_score
        return self.__children[index]

    def getChild(self, index: int) -> Node:
        return self.__children[index]

    @property
    def ChildNumber(self):
        return len(self.__children)


class Leaf(Node):

    def __init__(self, table: list[list[str]]):
        super(Leaf, self).__init__(table)
        self.CalculateScore()

    def CalculateScore(self):
        winner = TicTacToe.GameIsEnd(self.table)
        if not winner:
            self.score = 0
        if winner == Users.Player:
            self.score = -5
        if winner == Users.AI:
            self.score = 10
        if self.parent:
            self.parent.CalculateScore()

    @property
    def IsLeaf(self) -> bool:
        return True