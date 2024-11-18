from tkinter import Tk, Button, Label, font, Radiobutton, StringVar

from DegugOutput import DebugOutput
from Game import Game, DebugGame
from setup import Users, MAIN_GRID, GAME_GRID, DEBUG_MOD, SETTINGS_GRID, LEVELS


class GameGUI(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("TicTacToe")
        self.minsize(360, 360)

        self.ai: bool = False
        self.step: str = Users.First
        self.game = None

        self.game_buttons: list[list[Button]] = [[]]
        self.game_label = None

        self.LARGE_FONT = font.Font(family="Helvetica", size=40, weight="bold")
        self.MIDDLE_FONT = font.Font(family="Helvetica", size=10, weight="bold")

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

    def AIInput(self):
        DebugOutput.print("AIInput")

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

        if self.game.ai_strategy and self.game.IsRun:
            self.AIInput()

    def SetGridConfig(self, rows: list[tuple[int, int]], columns: list[tuple[int, int]]) -> None:
        for row_index, row_weight in rows:
            self.grid_rowconfigure(row_index, weight=row_weight)
        for column_index, column_weight in columns:
            self.grid_columnconfigure(column_index, weight=column_weight)

    # noinspection PyTypeChecker,PyUnresolvedReferences
    def CreateGameGrid(self):
        self.SetGridConfig(*GAME_GRID)

        self.game_buttons = [[None, None, None],
                             [None, None, None],
                             [None, None, None]]

        for i in range(3):
            for j in range(3):
                self.game_buttons[i][j] = Button(self, text="",
                    command=lambda position = (i, j): GameGUI.PlayerInput(self, position),
                    font=self.MIDDLE_FONT)
                self.game_buttons[i][j].grid(row=i + 1, column=j + 1, sticky="nsew")

        Button(self, text="quit", command=self.MainMenu).grid(row=4, column=0, columnspan=5)

        self.game_label = Label(self, text="Hello world", font=self.LARGE_FONT)
        self.game_label.grid(row = 0, column=0, columnspan=5)

    def AISettingsScreen(self):
        self.ClearWindow()
        self.SetGridConfig(*SETTINGS_GRID)

        step_choice = StringVar(None, Users.First)
        level_choice = StringVar(None, "normal")

        Label(self, text="How is first?", font=self.MIDDLE_FONT).grid(row = 0, column = 0)
        Radiobutton(self, text='Player', variable=step_choice, value=Users.First, font=self.MIDDLE_FONT).grid(row=0, column=1)
        Radiobutton(self, text='AI', variable=step_choice, value=Users.Second, font=self.MIDDLE_FONT).grid(row=0, column=2)

        Label(self, text="level: ", font=self.MIDDLE_FONT).grid(row=2, column=0)
        for i, key in enumerate(LEVELS.keys()):
            Radiobutton(self, text=key, variable=level_choice, value=key, font=self.MIDDLE_FONT).grid(
                row=i + 2, column=1, sticky="W")

        (Button(self, text="Start game", command=lambda :self.PvAImode(step_choice.get(), level_choice.get())).
         grid(column=0, columnspan=4, row=3+len(LEVELS)))

        self.mainloop()

    def PvAImode(self, step: str, level_choice: str):
        self.game = DebugGame() if DEBUG_MOD else Game()
        self.step = step
        self.game.planed_steps = LEVELS[level_choice]
        DebugOutput.print("Game init: ", self.step, " ", self.game.planed_steps)

        self.game.AIinit(self.step)
        if self.step == Users.Second:
            self.step = Users.First

        self.ClearWindow()
        self.CreateGameGrid()
        self.RenderGameGrid()

    def PvPMode(self):
        self.ClearWindow()
        self.CreateGameGrid()
        self.game = Game()
        self.game.ai_strategy = None
        self.RenderGameGrid()

    def MainMenu(self):
        self.ClearWindow()

        self.SetGridConfig(*MAIN_GRID)

        Label(self, text="Python TicTacToe!!!", font=self.LARGE_FONT).grid(row=0, column=0, columnspan=2, sticky="nsew")
        Button(self, text="mode PvP", command=self.PvPMode).grid(row=1, column=0, sticky="nsew")
        Button(self, text="mode PvAI", command=self.AISettingsScreen).grid(row=1, column=1, sticky="nsew")

        self.mainloop()