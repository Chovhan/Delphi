import numpy as np
import random as rnd


def create_random_array():
    array = np.zeros((2, 10), dtype=int)
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = rnd.randint(0, 1000)
    return array


def reshape_array(array):
    one_dimensional_array = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            one_dimensional_array.append(array[i, j])
    return one_dimensional_array


def partition(sort_list, bottom, top):
    i = (bottom - 1)
    pivot = sort_list[top]
    for j in range(bottom, top):
        if sort_list[j] <= pivot:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i + 1], sort_list[top] = sort_list[top], sort_list[i + 1]
    return i + 1


def quick_sort(sort_list, bottom, top):
    if bottom < top:
        pi = partition(sort_list, bottom, top)
        quick_sort(sort_list, bottom, pi - 1)
        quick_sort(sort_list, pi + 1, top)


array = reshape_array(create_random_array())
print("Early array: " + str(array))
bottom_line = 0
top_line = len(array) - 1
quick_sort(array, bottom_line, top_line)
print("Sorted array: " + str(array))
