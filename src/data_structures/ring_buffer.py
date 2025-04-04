import ctypes
import typing as tp

T = tp.TypeVar("T")


class FIFORingBuffer(tp.Generic[T]):
    def __init__(self) -> None:
        self._length = 0
        self._capacity = 10
        self._array = self._create_array(self._capacity)
        self._head = 0
        self._tail = 0

    def _create_array(self, size: int) -> ctypes.Array[T]:
        ArrayType = size * ctypes.py_object
        return ArrayType()

    def enqueue(self, value: T) -> None:
        self._length += 1
        if self._tail == self._capacity:
            self._tail = 0
            self._array[self._tail] = value

        else:
            self._array[self._tail] = value
            self._tail += 1

        

    def dequeue(self) -> T:
        value = self._array[self._head]
        self._array[self._head] = None
        if self._head == self._capacity:
            self._head = 0
        else:
            self._head += 1
        self._length -= 1
        return value
