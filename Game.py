from TicTacToeTreeBuilder import TicTacToeTreeBuilder
from TicTacToe import TicTacToe
from setup import Users, SPACE, print_table
from TicTacToTree import Root

class Game:

    def __init__(self):
        self.table = [
            [SPACE] * 3,
            [SPACE] * 3,
            [SPACE] * 3
        ]
        self.ai_strategy: Root | None = None
        self.__game_cycle = False

    def AIStep(self):
        best_ai_state = self.ai_strategy.getBestChild()
        self.ai_strategy = best_ai_state
        self.table = self.ai_strategy.table

    def UpdateAI(self):
        self.ai_strategy = self.ai_strategy.findChild(self.table)

    def __GameStop(self):
        self.__game_cycle = False

    def __GameUpdate(self):
        print_table(self.table)
        x, y = [int(x) for x in input("Position (x, y): ").split(", ")]

        if not (1 <= x <= 3) or not (1 <= y <= 3) or self.table[y - 1][x - 1] != SPACE:
            return

        self.table[y - 1][x - 1] = Users.Player

        print_table(self.table)
        if TicTacToe.checkGame(self.table):
            self.__GameStop()
            return

        self.UpdateAI()
        self.AIStep()

        if TicTacToe.checkGame(self.table):
            self.__GameStop()

    def GameStart(self):
        self.__game_cycle = True
        choice = int(input("How is first?\n1. user\n2. ai\n"))
        if choice == 1:
            self.ai_strategy = TicTacToeTreeBuilder.generate(self.table, Users.Player)
        elif choice == 2:
            self.ai_strategy = TicTacToeTreeBuilder.generate(self.table, Users.AI)
            self.AIStep()
        else:
            return

        while self.__game_cycle:
            self.__GameUpdate()

        print_table(self.table)
        winner = TicTacToe.checkGame(self.table)
        if winner == "draw":
            print("DRAW!!!")
        else:
            print(winner, " WIN!")

class DebugGame(Game):

    def __init__(self):
        super(DebugGame, self).__init__()

    def UpdateAI(self):
        super(DebugGame, self).UpdateAI()
        for j in range(3):
            for i in range(self.ai_strategy.ChildNumber):
                print(self.ai_strategy.getChild(i).table[j], end=" ")
            print()
        for i in range(self.ai_strategy.ChildNumber):
            print(f"{self.ai_strategy.getChild(i).score:15.3f}", end=" ")
        print()
        