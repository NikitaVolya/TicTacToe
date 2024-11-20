from enum import Enum

from Pointer import Pointer
from typing import Callable

class Table:

    def __init__(self, data: list[list[any]] = None):
        self._data: list[list[any]] = []
        self.__height: int = 0
        self.__width: int = 0
        if data:
            self.set(data)

    def set(self, value: list[list[any]]) -> 'Table':
        self._data = []
        self.__height = len(value)
        self.__width = len(value[0])
        for row in value:
            if self.__width != len(row):
                raise Exception("")
            self._data.append(row.copy())
        return self

    def copyOf(self, other: 'Table') -> 'Table':
        for i in range(self.Height):
            for j in range(self.Width):
                self[i, j] = other[i, j]
        return self

    def copyTo(self, other: 'Table'):
        return other.copyOf(self)

    def copy(self) -> 'Table':
        return Table(self._data)

    @property
    def Height(self) -> int:
        return self.__height

    @property
    def Width(self) -> int:
        return self.__width

    def Map(self, func: Callable[[any], any]) -> 'Table':
        for i in range(self.__height):
            for j in range(self.__width):
                self[i, j] = func(self[i, j])
        return self

    def Foreach(self, func: Callable[[any], None]) -> 'Table':
        for i in range(self.Height):
            for j in range(self.Width):
                func(self[i, j])
        return self

    def First(self, func: Callable[[any], bool]) -> any:
        for i in range(self.__height):
            for j in range(self.__width):
                if func(self[i, j]):
                    return self[i, j]
        return None

    def Count(self, element: any) -> int:
        counter = Pointer(0)

        def check(x):
            if x == element:
                counter.Value += 1

        self.Foreach(check)
        return counter.Value

    def MaxOfAll(self, func: Callable[[any, any], bool]) -> any:
        rep = Pointer(self._data[0][0])
        def max_function(element):
            if func(element, rep.Value):
                rep.Value = element
        self.Foreach(max_function)
        return rep.Value

    @property
    def Max(self) -> any:
        return self.MaxOfAll(lambda a, b: a > b)

    @property
    def Min(self) -> any:
        return self.MaxOfAll(lambda a, b: a < b)

    def FindIndex(self, element: any, index: int = 0, number: int = 0) -> (int, int):
        i = Pointer(0)
        n = Pointer(number)
        def check(x):
            if i.Value < index:
                pass
            elif x == element and n.Value > 0:
                n.Value -= 1
            elif x == element:
                return True
            i.Value += 1
            return False
        if not self.First(check):
            return -1
        return i.Value // self.__width, i.Value % self.__width

    def __str__(self) -> str:
        def step(element, text_pointer, index):
            text_pointer.Value += str(element) + " "
            index.Value += 1
            if index.Value % self.__width == 0:
                text_pointer.Value += "|\n|"
        text = Pointer("|")
        i = Pointer(0)
        self.Foreach(lambda x: step(x, text, i))
        return text.Value[:-2]

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: 'Table') -> bool:
        if self.__height != other.__height or self.__width != other.__width:
            return False
        for i in range(self.__height):
            for j in range(self.__width):
                if self[i, j] != other[i, j]:
                    return False
        return True

    def Equal(self, other: 'Table'):
        return self == other or \
            MirrorTable(self, Rotate.HORIZONTAL) == other or \
            MirrorTable(self, Rotate.VERTICAL) == other or \
            MirrorTable(self, Rotate.HORIZONTAL_VERTICAL) == other or\
            MirrorTable(self, Rotate.SYMMETRIC) == other


    def GetRotate(self, other: 'Table'):
        if self == MirrorTable(other, Rotate.HORIZONTAL):
            return Rotate.HORIZONTAL
        elif self == MirrorTable(other, Rotate.VERTICAL):
            return Rotate.VERTICAL
        elif self == MirrorTable(other, Rotate.HORIZONTAL_VERTICAL):
            return Rotate.HORIZONTAL_VERTICAL
        elif self == MirrorTable(other, Rotate.SYMMETRIC):
            return Rotate.SYMMETRIC
        else:
            return -1

    def __getitem__(self, index_couple: tuple[int, int]) -> any:
        row, colum = index_couple
        assert 0 <= row < self.__height
        assert 0 <= colum < self.__width
        return self._data[row][colum]

    def __setitem__(self, index_couple: tuple[int, int], value):
        row, colum = index_couple
        assert 0 <= row < self.__height
        assert 0 <= colum < self.__width
        self._data[row][colum] = value


class Rotate(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    HORIZONTAL_VERTICAL = 2
    SYMMETRIC = 3

class MirrorTable(Table):

    def __init__(self, table: Table, state = Rotate.HORIZONTAL):
        super(Table, self).__init__()
        self.set(table._data)
        self.__state = state

    def __getitem__(self, index_couple: tuple[int, int]):
        row, column = index_couple
        if self.__state == Rotate.VERTICAL:
            return self._data[self.Height - 1 - row][column]
        elif self.__state == Rotate.HORIZONTAL:
            return self._data[row][self.Width - 1 - column]
        elif self.__state == Rotate.HORIZONTAL_VERTICAL:
            return self._data[self.Height - 1 - row][self.Width - 1 - column]
        elif self.__state == Rotate.SYMMETRIC:
            return self._data[column][row]




if __name__ == "__main__":

    a = Table([["x", " ", " "], [" ", "o", " "], [" ", " ", " "]])
    b = Table([[" ", " ", " "], [" ", "o", " "], [" ", " ", "x"]])
    print(a)
    print(b)
    print(a.GetRotate(b))
    print(MirrorTable(a, b.GetRotate(a)))