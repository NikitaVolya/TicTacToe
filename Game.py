from msilib import Table

from PIL.ImageOps import mirror

from TicTacToeTreeBuilder import TicTacToeTreeBuilder
from TicTacToe import TicTacToe
from setup import Users, SPACE
from TicTacToTree import Root
from Table import Table, MirrorTable


class Game:

    def __init__(self):
        self.table: Table = Table(
            [[SPACE] * 3,
            [SPACE] * 3,
            [SPACE] * 3]
        )
        self.ai_strategy: Root = None
        self.planed_steps = 5
        self.__game_cycle = True

    def PlayerStep(self, position: tuple[int, int], symbl: str = Users.First) -> bool:
        x, y = position
        if not (0 <= x <= 2) or not (0 <= y <= 2) or self.table[x, y] != SPACE:
            return False

        self.table[x, y] = symbl
        return True

    def AIStep(self):
        best_ai_state = self.ai_strategy.getBestChild()
        if best_ai_state is None:
            raise "Ai strategy not found"

        rotate = self.ai_strategy.TablePtr.GetRotate(self.table)
        self.ai_strategy = best_ai_state
        self.table = self.ai_strategy.Table
        if rotate != -1:
            tmp = MirrorTable(self.ai_strategy.Table, rotate)
            tmp.copyTo(self.table)

        TicTacToeTreeBuilder.generate(self.ai_strategy, Users.First)


    def UpdateAI(self):
        self.ai_strategy = self.ai_strategy.findChild(self.table)

    def CheckGameOver(self) -> bool:
        if TicTacToe.checkGame(self.table):
            self.__game_cycle = False
            return True
        return False

    def __GameUpdate(self):
        print(self.table)
        x, y = [int(x) for x in input("Position (x, y): ").split(", ")]

        if not self.PlayerStep((x, y)) or self.CheckGameOver():
            return

        self.UpdateAI()
        self.AIStep()

        self.CheckGameOver()

    @property
    def IsRun(self) -> bool:
        self.CheckGameOver()
        return self.__game_cycle

    def AIinit(self, first_symbl: str = Users.First):
        self.ai_strategy = Root(self.table)
        TicTacToeTreeBuilder.generate(self.ai_strategy, first_symbl, self.planed_steps)
        if first_symbl == Users.Second:
            self.AIStep()

    def AIDestroy(self):
        self.ai_strategy = None

    def GameOverText(self):
        winner = TicTacToe.checkGame(self.table)
        if winner == "draw":
            return "DRAW!!!"
        elif winner:
            return winner + " WIN!"
        return ""

    def GameStart(self):
        self.__game_cycle = True
        choice = Users.First if int(input("How is first?\n1. user\n2. ai\n")) == 1 else Users.Second
        self.AIinit(choice)

        while self.__game_cycle:
            self.__GameUpdate()

        print(self.table)
        print(self.GameOverText())

class DebugGame(Game):

    def __init__(self):
        super(DebugGame, self).__init__()

    def UpdateAI(self):
        super(DebugGame, self).UpdateAI()
        for i in range(self.ai_strategy.ChildNumber):
            print(self.ai_strategy.getChild(i).Table, end=" ")
            print(f"{self.ai_strategy.getChild(i).Score:15.3f}\n")
        print()
        