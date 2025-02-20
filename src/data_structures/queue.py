from __future__ import annotations

import typing as tp
from dataclasses import dataclass, field

T = tp.TypeVar("T")


@dataclass
class QueueNode:
    value: T
    next: "QueueNode" | None = field(default=None, init=False)


class Queue(tp.Generic[T]):
    def __init__(self) -> None:
        self._head: QueueNode | None = None
        self._tail: QueueNode | None = None
        self._lenght: int = 0

    def enqueue(self, value: T) -> None:
        self._lenght += 1
        node = QueueNode(value=value)
        if self._lenght == 0:
            self._head = node
            self._tail = node
            return

        self._tail.next = node
        self._tail = node

    def dequeue(self) -> T | None:
        if self._head is None:
            return None

        self._lenght -= 1
        current_head = self._head
        self._head = current_head.next
        current_head.next = None
        return current_head.value

    def peek(self) -> T | None:
        if self._head is None:
            return None

        return self._head.value
