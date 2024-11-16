from logging import raiseExceptions
from random import choice

from TicTacToe import TicTacToe
from setup import Users, AI_SCORE_FOR_DRAW, AI_SCORE_FOR_LOSE, AI_SCORE_FOR_WIN, PLANNED_STEPS
from Table import Table

class Node:

    def __init__(self, table: Table):
        self._parent: Node | None = None
        self._table: Table = table.copy()
        self._score = 0

    def deleteParent(self):
        self._parent = None

    def setParent(self, value: 'Node'):
        self._parent = value

    def CalculateScore(self):
        pass

    @property
    def Parent(self) -> 'Node':
        return self._parent

    @property
    def Score(self) -> int:
        return self._score

    @property
    def Table(self):
        return self._table.copy()

    @property
    def IsLeaf(self) -> bool:
        return False


class Root(Node):

    def __init__(self, table: Table):
        self.__children: [Node] = []
        super(Root, self).__init__(table)

    def CalculateScore(self):
        rep: int = 0
        for node in self.__children:
            rep += node.Score / PLANNED_STEPS
        self._score = rep

        if self.Parent:
            self.Parent.CalculateScore()

    def appChild(self, child: Node):
        self.__children.append(child)
        child.setParent(self)
        self.CalculateScore()


    def findChild(self, table: Table):
        for child in self.__children:
            if child.Table == table:
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
        if self._parent:
            self._parent.CalculateScore()

    @property
    def IsLeaf(self) -> bool:
        return True