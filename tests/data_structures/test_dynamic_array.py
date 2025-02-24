
import pytest
from rich import print  # noqa

from src.data_structures.dynamic_array import DynamicArray


def test_append_to_add_a_new_value_in_the_array():
    arr = DynamicArray()
    value = 1
    arr.append(value)

    assert arr[0] == value


def test_append_to_increase_the_length_of_the_array():
    arr = DynamicArray()
    initial_length = len(arr)

    value = 1
    arr.append(value)

    assert len(arr) == initial_length + 1


def test_append_to_double_the_capacity_of_the_array_when_full():
    arr = DynamicArray()
    initial_capacity = arr._capacity

    for i in range(initial_capacity + 1):
        arr.append(i)

    assert arr._capacity == initial_capacity * 2


def test_getitem_to_return_the_value_at_the_given_index():
    arr = DynamicArray()
    value = 1
    arr.append(value)

    assert arr[0] == value


def test_getitem_to_raise_an_error_when_the_index_is_out_of_range():
    arr = DynamicArray()

    with pytest.raises(IndexError):
        arr[0]


def test_setitem_to_update_the_value_at_the_given_index():
    arr = DynamicArray()
    value = 1
    arr.append(value)

    new_value = 2
    arr[0] = new_value

    assert arr[0] == new_value


def test_setitem_to_raise_an_error_when_the_index_is_out_of_range():
    arr = DynamicArray()

    with pytest.raises(IndexError):
        arr[0] = 1


def test_resize_to_double_the_capacity_of_the_array():
    arr = DynamicArray()
    initial_capacity = arr._capacity
    
    arr._resize()
    
    assert arr._capacity == initial_capacity * 2



def test_resize_to_create_an_array_with_the_lenght_of_capacity():
    arr = DynamicArray()
    
    arr._resize()

    assert len(arr._array) == arr._capacity



def test_resize_to_copy_the_values_to_the_new_array():
    arr = DynamicArray()
    values = [1, 2, 3, 4]

    for value in values:
        arr.append(value)

    arr._resize()

    for i, value in enumerate(values):
        assert arr[i] == value


def test_create_array_to_return_an_array_of_the_given_size():
    arr = DynamicArray()
    size = 4

    array = arr._create_array(size)

    assert len(array) == size
