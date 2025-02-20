from __future__ import annotations

import typing as tp
from dataclasses import dataclass

T = tp.TypeVar("T")


@dataclass
class StackNode(tp.Generic[T]):
    value: T
    previous: "StackNode" | None = None


class Stack(tp.Generic[T]):
    def __init__(self) -> None:
        self._head: StackNode | None = None
        self._lenght: int = 0

    def append(self, value: T) -> None:
        self._lenght += 1
        node = StackNode(value=value)
        if self._head is None:
            self._head = node
            return

        current_head = self._head
        node.previous = current_head
        self._head = node

    def pop(self) -> T | None:
        if self._head is None:
            return None
        
        self._lenght -= 1
        current_head = self._head
        self._head = current_head.previous
        current_head.previous = None
        return current_head.value

    def peek(self) -> T:
        if self._head is None:
            return None

        return self._head.value
