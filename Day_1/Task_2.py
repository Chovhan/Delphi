import numpy as np
import random as rnd


def create_random_array():
    array = np.zeros((2, 10), dtype=int)
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = rnd.randint(0, 10)
    return array


def reshape_array(array):
    one_dimensional_array = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            one_dimensional_array.append(array[i, j])
    return one_dimensional_array


def bubble_sort(array):
    array_len = len(array)
    for i in range(array_len):
        for j in range(0, array_len - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def delete_iteration(array):
    no_iterations_array = []
    for i in array:
        if i not in no_iterations_array:
            no_iterations_array.append(i)
    return no_iterations_array


array = reshape_array(create_random_array())
print("Early array: " + str(array))
bottom_line = 0
top_line = len(array) - 1
print("Sorted array: " + str(bubble_sort(delete_iteration(array))))
