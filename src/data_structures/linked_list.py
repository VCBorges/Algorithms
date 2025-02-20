from __future__ import annotations

import typing as tp
from dataclasses import dataclass

T = tp.TypeVar("T")


@dataclass
class SinglyNode(tp.Generic[T]):
    value: T
    next: "SinglyNode" | None = None


class SinglyLinkedList(tp.Generic[T]):
    def __init__(self, value: T):
        self._lenght: int = 0
        self.head: SinglyNode = self._create_node(value)

    def __iter__(self) -> T:
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __getitem__(self, index: int) -> T:
        if index >= len(self):
            raise IndexError("Index out of range")

        if index == 0:
            return self.head.value

        node = self._get_node_at(index)
        return node.value

    def __len__(self) -> int:
        return self._lenght

    def __repr__(self):
        return f"<{self.__class__.__name__}({[i for i in self]})>"

    def append(self, value: T) -> None:
        new_node = self._create_node(
            value=value,
            next_node=self.head,
        )
        self.head = new_node

    def insert(self, index: int, value: T) -> None:
        if index == 0:
            self.append(value)
            return

        previous_node = self._get_node_at(index - 1)
        next_node = previous_node.next

        previous_node.next = self._create_node(
            value=value,
            next_node=next_node,
        )

    def pop(self) -> T:
        removed_node = self.head
        self.head = self.head.next
        self._lenght -= 1
        return removed_node

    def remove(self, index: int) -> None:
        if index == 0:
            self.pop()
            return

        previous_node = self._get_node_at(index - 1)
        next_node = previous_node.next.next

        previous_node.next = next_node
        self._lenght -= 1

    def _create_node(self, value: T, next_node: SinglyNode | None = None) -> SinglyNode:
        self._lenght += 1
        return SinglyNode(
            value=value,
            next=next_node,
        )

    def _get_node_at(self, index: int) -> SinglyNode:
        count = 0
        current = self.head
        while count < index:
            current = current.next
            count += 1

        return current
