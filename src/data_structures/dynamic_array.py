import ctypes
import typing as tp

T = tp.TypeVar("T")

class DynamicArray(tp.Generic[T]):
    def __init__(self) -> None:
        self._length = 0
        self._capacity = 4
        self._array = self._create_array(self._capacity)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}({[self._array[i] for i in range(self._length)]})>"

    def __str__(self) -> str:
        return self.__repr__()

    def __len__(self) -> int:
        return self._length

    def __getitem__(self, index: int) -> T:
        if index > (self._length - 1):
            raise IndexError("Index out of range")
        return self._array[index]

    def __setitem__(self, index: int, value: T) -> None:
        if index > (self._length - 1):
            raise IndexError("Index out of range")
        self._array[index] = value

    def _create_array(self, size: int) -> ctypes.Array[ctypes.py_object]:
        ArrayType = size * ctypes.py_object
        return ArrayType()

    def _resize(self) -> None:
        self._capacity *= 2
        resized_array = self._create_array(self._capacity)
        for i in range(self._length):
            resized_array[i] = self._array[i]
        self._array = resized_array

    def append(self, value: T) -> T:
        if self._length == self._capacity:
            self._resize()
        self._array[self._length] = value
        self._length += 1
