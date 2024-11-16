from idlelib.pyshell import usage_msg
from tkinter import Tk, Button, Label, font
from Game import Game, DebugGame
from setup import Users, MAIN_GRID, GAME_GRID, DEBUG_MOD


class GameGUI(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("TicTacToe")
        self.minsize(720, 720)

        self.ai: bool = False
        self.step: str = Users.First
        self.game = None

        self.game_buttons: list[list[Button]] = [[]]
        self.game_label = None

        self.LARGE_FONT = font.Font(family="Helvetica", size=40, weight="bold")

    def AIInput(self):
        print("AIInput")
        self.game.UpdateAI()
        self.game.AIStep()
        self.step = Users.First
        self.RenderGameGrid()

    def PlayerInput(self, position: tuple[int, int]):
        if not self.game.IsRun:
            return
        if not self.game.PlayerStep(position, self.step):
            return

        self.step = Users.switch(self.step)
        self.RenderGameGrid()

        if self.AI and self.game.IsRun:
            print(self.AI)
            self.AIInput()

    def SetGridConfig(self, rows: list[tuple[int, int]], columns: list[tuple[int, int]]) -> None:
        for row_index, row_weight in rows:
            self.grid_rowconfigure(row_index, weight=row_weight)
        for column_index, column_weight in columns:
            self.grid_columnconfigure(column_index, weight=column_weight)

    def ClearWindow(self):
        for widget in self.winfo_children():
            widget.destroy()

    def RenderGameGrid(self):
        self.game_label.config(text=self.step)
        for i in range(3):
            for j in range(3):
                self.game_buttons[i][j].config(text=self.game.table[i, j])

        if not self.game.IsRun:
            self.game_label.config(text=self.game.GameOverText())

    # noinspection PyTypeChecker,PyUnresolvedReferences
    def CreateGameGrid(self):
        self.SetGridConfig(*GAME_GRID)

        self.game_buttons = [[None, None, None],
                             [None, None, None],
                             [None, None, None]]

        for i in range(3):
            for j in range(3):
                self.game_buttons[i][j] = Button(self, text="",
                    command=lambda position = (i, j): GameGUI.PlayerInput(self, position))
                self.game_buttons[i][j].grid(row=i + 1, column=j + 1, sticky="nsew")

        quit_button = Button(self, text="quit", command=self.MainMenu)
        quit_button.grid(row=4, column=0, columnspan=5)

        self.game_label = Label(self, text="Hello world", font=self.LARGE_FONT)
        self.game_label.grid(row = 0, column=0, columnspan=5)

    @property
    def AI(self):
        return self.ai

    @AI.setter
    def AI(self, value: bool):
        if self.ai != value:
            if value:
                print("AI Init")
                self.game.AIinit(self.step)
            else:
                self.game.AIDestroy()
            print(value)
            self.ai = value

    def PvAImode(self):

        self.ClearWindow()
        self.CreateGameGrid()

        if self.game:
            self.AI = False
            self.game = None

        if DEBUG_MOD:
            self.game = DebugGame()
        else:
            self.game = Game()

        self.AI = True
        if self.step == Users.Second:
            self.step = Users.First

        self.RenderGameGrid()

    def PvPMode(self):
        self.ClearWindow()
        self.CreateGameGrid()
        self.game = Game()

        self.AI = False

        self.RenderGameGrid()

    def MainMenu(self):
        self.ClearWindow()

        self.SetGridConfig(*MAIN_GRID)

        main_label = Label(self, text="Python TicTacToe!!!", font=self.LARGE_FONT)
        pvp_button = Button(self, text="mode PvP", command=self.PvPMode)
        pvai_button = Button(self, text="mode PvAI", command=self.PvAImode)

        main_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
        pvp_button.grid(row=1, column=0, sticky="nsew")
        pvai_button.grid(row=1, column=1, sticky="nsew")

        self.mainloop()