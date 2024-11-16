
class Users:
    First: str = "X"
    Second: str = "O"

    @staticmethod
    def switch(point: str):
        if point == Users.First:
            return Users.Second
        if point == Users.Second:
            return Users.First
        return None

SPACE = " "
DEBUG_MOD = True
AI_SCORE_FOR_WIN = 10
AI_SCORE_FOR_LOSE = -5
AI_SCORE_FOR_DRAW = 0
PLANNED_STEPS = 5 # 2 -> dump
                  # 4 -> easy
                  # 5 -> normal
                  # 6 -> hard
                  # 7 -> impossible

MAIN_GRID = [
    [(0, 1), (1, 2), (2, 1), (3, 0), (4, 0)],
    [(0, 1), (1, 1), (2, 0), (3, 0), (4, 0)]
]

GAME_GRID = [
    [(0, 1), (1, 2), (2, 2), (3, 2), (4, 1)],
    [(0, 1), (1, 2), (2, 2), (3, 2), (4, 1)]
]