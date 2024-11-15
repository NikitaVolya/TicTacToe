from Game import Game, DebugGame
from setup import DEBUG_MOD

if __name__ == "__main__":
    if DEBUG_MOD:
        game = DebugGame()
    else:
        game = Game()
    game.GameStart()
