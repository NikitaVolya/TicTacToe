
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
DEBUG_MOD = False
AI_SCORE_FOR_WIN = 100
AI_SCORE_FOR_LOSE = -50
AI_SCORE_FOR_DRAW = 0
LEVELS  = {
            "dumb": 2,
            "easy": 4,
            "normal": 5,
            "hard": 7,
            "impossible": 9
        }

MAIN_GRID = [
    [(0, 1), (1, 2), (2, 1), (3, 0), (4, 0)],
    [(0, 1), (1, 1), (2, 0), (3, 0), (4, 0)]
]

GAME_GRID = [
    [(0, 1), (1, 2), (2, 2), (3, 2), (4, 1)],
    [(0, 1), (1, 2), (2, 2), (3, 2), (4, 1)]
]

SETTINGS_GRID = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 1), (2, 1), (3, 2)]
]