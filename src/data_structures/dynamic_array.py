import ctypes
from typing import Any


class DynamicArray:
    def __init__(self) -> None:
        self._lenght = 0
        self._capacity = 4
        self._array = self._create_array(self._capacity)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}({[self._array[i] for i in range(self._lenght)]})>"

    def __str__(self) -> str:
        return self.__repr__()

    def __len__(self) -> int:
        return self._lenght

    def __getitem__(self, index: int) -> Any:
        if index > self._lenght - 1:
            raise ValueError("Index out of range")
        return self._array[index]

    def __setitem__(self, index: int, value: Any) -> None:
        if index > self._lenght - 1:
            raise ValueError("Index out of range")
        self._array[index] = value

    @staticmethod
    def _create_array(size: int) -> ctypes.Array[ctypes.py_object]:
        ArrayType = size * ctypes.py_object
        return ArrayType()

    def _resize(self) -> None:
        self._capacity *= 2
        resized_array = self._create_array(self._capacity * 2)
        for i in range(self._lenght):
            resized_array[i] = self._array[i]
        self._array = resized_array
        print(f"The array was resized for a {self._capacity} capacity")

    def append(self, value: Any) -> None:
        if self._lenght == self._capacity:
            self._resize()
        self._array[self._lenght] = value
        self._lenght += 1
