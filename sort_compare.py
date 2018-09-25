#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment4 - Sort and Compare.  Tested in Python 2.7.15"""

import random
import time

def insertion_sort(a_list):
    """This is a insertion sort function.
    Args:
        a_list (list): A list contenting positive integers
    Returns:
        timecal (tuple): How long function took to calculate.
    """

    start = time.time()
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    return time.time() - start

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

def shell_sort(a_list):
    """This is shell sort function.

    Args:
        a_list (list): A list contenting positive integers

    Returns:
        timecal (tuple): How long function took to calculate.
   """
    start = time.time()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2
    return time.time() - start

def python_sort(a_list):
    """This is a python sort function.
    Args:
        a_list (list): A list contenting positive integers
    Returns:
        timecal (tuple): How long function took to calculate.
   """
    start = time.time()
    a_list.sort()
    return time.time() - start

def generate_random_list(total_lists, list_length):
    mylists = []
    for i in range(total_lists):
        a_list = range(list_length)
        random.shuffle(a_list)
        mylists.append(a_list)
    return mylists


if __name__ == '__main__':

    num_of_list = 100
    sort_functions = [(insertion_sort,"Insertion Sort"), (shell_sort,"Shell Sort"),
                         (python_sort,"Python Sort")]
    list_sizes = [500, 1000, 10000]

    for list_size in list_sizes:

        sum_of_search_time_list = []

        for i in range(len(sort_functions)):
            sum_of_search_time_list.append(0.0)

        print("List of size %d:"%(list_size))

        for i in range(num_of_list):

            a_list = generate_random_list(num_of_list, list_size)

            for x, function_tuple in enumerate(sort_functions):
                function, name = function_tuple
                list_copy = a_list[:]
                duration = function(list_copy)
                sum_of_search_time_list[x] += duration

        for x, function_tuple in enumerate(sort_functions):
            function, name = function_tuple
            print("    %s took %10.7f seconds to run, on average"%(name, (sum_of_search_time_list[x]/num_of_list)))
