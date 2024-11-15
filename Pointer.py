

class Pointer:

    def __init__(self, value: any):
        self.__value = value

    @property
    def Value(self):
        return self.__value

    @Value.setter
    def Value(self, value: any):
        self.__value = value
