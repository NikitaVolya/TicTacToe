from setup import DEBUG_MOD


class DebugOutput:

    def __init__(self):
        pass

    @staticmethod
    def print(*values, **kwargs):
        if not DEBUG_MOD:
            return
        print(*values, *kwargs)