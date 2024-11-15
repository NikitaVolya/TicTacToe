
class Users:
    Player: str = "X"
    AI: str = "O"

    @staticmethod
    def switch(point: str):
        if point == Users.Player:
            return Users.AI
        if point == Users.AI:
            return Users.Player
        return None

SPACE = " "
DEBUG_MOD = True
AI_SCORE_FOR_WIN = 10
AI_SCORE_FOR_LOSE = -5
AI_SCORE_FOR_DRAW = 0
PLANNED_STEPS = 2 # 2 -> dump 3-4 -> very easy 5 -> normal 6 -> hard 7-9 impossible