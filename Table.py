from Pointer import Pointer
from typing import Callable

class Table:

    def __init__(self, data: list[list[any]]):
        self.__data: list[list[any]] = []
        self.__height: int = 0
        self.__width: int = 0
        self.set(data)

    def set(self, value: list[list[any]]) -> 'Table':
        self.__data = []
        self.__height = len(value)
        self.__width = len(value[0])
        for row in value:
            if self.__width != len(row):
                raise Exception("")
            self.__data.append(row.copy())
        return self

    def copyOf(self, other: 'Table') -> 'Table':
        return self.set(other.__data)

    def copyTo(self, other: 'Table'):
        return other.set(self.__data)

    def copy(self) -> 'Table':
        return Table(self.__data)

    @property
    def Height(self) -> int:
        return self.__height

    @property
    def Width(self) -> int:
        return self.__width

    def Map(self, func: Callable[[any], any]) -> 'Table':
        for i in range(self.__height):
            for j in range(self.__width):
                self.__data[i][j] = func(self.__data[i][j])
        return self

    def Foreach(self, func: Callable[[any], None]) -> 'Table':
        for i in range(self.__height):
            for j in range(self.__width):
                func(self.__data[i][j])
        return self

    def First(self, func: Callable[[any], bool]) -> any:
        for i in range(self.__height):
            for j in range(self.__width):
                if func(self.__data[i][j]):
                    return self.__data[i][j]
        return None

    def Count(self, element: any) -> int:
        counter = Pointer(0)
        def check(x):
            if x == element:
                counter.Value += 1
        self.Foreach(check)
        return counter.Value

    def MaxOfAll(self, func: Callable[[any, any], bool]) -> any:
        rep = Pointer(self.__data[0][0])
        def max_function(element):
            if func(element, rep.Value):
                rep.Value = element
        self.Foreach(max_function)
        return rep.Value

    @property
    def Max(self, func = lambda a, b: a > b) -> any:
        return self.MaxOfAll(func)

    @property
    def Min(self, func = lambda a, b: a < b) -> any:
        return self.MaxOfAll(func)

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
                if self.__data[i][j] != other.__data[i][j]:
                    return False
        return True

    def __getitem__(self, index_couple: tuple[int, int]) -> any:
        row, colum = index_couple
        assert 0 <= row < self.__height
        assert 0 <= colum < self.__width
        return self.__data[row][colum]

    def __setitem__(self, index_couple: tuple[int, int], value):
        row, colum = index_couple
        assert 0 <= row < self.__height
        assert 0 <= colum < self.__width
        self.__data[row][colum] = value

if __name__ == "__main__":

    a = Table([[1, 2, 3], [2, 3, 2], [5, 6, 7]])
    print(a[1, 1])
    print(a.FindIndex(2, number=2))