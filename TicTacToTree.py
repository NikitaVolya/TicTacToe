
from random import choice

from TicTacToe import TicTacToe
from setup import Users, AI_SCORE_FOR_DRAW, AI_SCORE_FOR_LOSE, AI_SCORE_FOR_WIN
from Table import Table

class Node:

    def __init__(self, table: Table):
        self._table: Table = table
        self._score = None
        self.Weight = 1

    def CalculateScore(self):
        pass

    @property
    def Score(self) -> int:
        if not self._score:
            self.CalculateScore()
        return self._score

    @property
    def Table(self):
        return self._table.copy()

    @property
    def TablePtr(self):
        return self._table

    @property
    def IsLeaf(self) -> bool:
        return False


class Root(Node):

    def __init__(self, table: Table):
        self.__children: [Node] = []
        super(Root, self).__init__(table)

    def CalculateScore(self) -> None:
        rep: int = 0
        for node in self.__children:
            rep += node.Score * node.Weight / 10
        self._score = rep

    def appChild(self, child: Node) -> None:
        self.__children.append(child)

    def findChild(self, table: Table) -> Node | None:
        for child in self.__children:
            if child.Table.Equal(table):
                return child
        return None

    def getBestChild(self) -> Node:
        if not self.__children:
            raise "Error"
        max_score = [self.__children[0]]
        for child in self.__children:
            if child.Score > max_score[0].Score:
                max_score = [child]
            elif child.Score == max_score[0].Score:
                max_score.append(child)
        return choice(max_score)

    def getChild(self, index: int) -> 'Root':
        return self.__children[index]

    @property
    def ChildNumber(self):
        return len(self.__children)


class Leaf(Node):

    def __init__(self, table: Table):
        super(Leaf, self).__init__(table)
        self.CalculateScore()

    def CalculateScore(self):
        winner = TicTacToe.GameIsEnd(self._table)
        if not winner:
            self._score = AI_SCORE_FOR_DRAW
        if winner == Users.First:
            self._score = AI_SCORE_FOR_LOSE
        if winner == Users.Second:
            self._score = AI_SCORE_FOR_WIN

    @property
    def IsLeaf(self) -> bool:
        return True