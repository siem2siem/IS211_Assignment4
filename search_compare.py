#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment4 - Search and Compare.  Tested in Python 2.7.15"""

import time
import random


def sequential_search(a_list, item):
    """This is a sequential search function.
    Args:
        a_list(list):  A list contenting data 
        item(mixed):   Item used for the search within the list
    Returns:
        (Tuple): time in seconds
    """
    start = time.time()
    pos = 0
    found = False
    
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    timecalc = end - start

    if not found:
        pos = -1

    return (pos, timecalc)

def ordered_sequential_search(a_list, item):
    """This is a ordered sequential search function.
    Args:
        a_list(list):  A list contenting positive integers 
        item(mixed):   Item used for the search within the list
    Returns:
        (Tuple): time in seconds
    """
    a_list.sort()
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    timecalc = end - start

    if not found:
        pos = -1

    return (pos, timecalc)


def binary_search_iterative(a_list, item):
    """This is a binary search iterative function.
    Args:
        a_list(list):  A list contenting positive integers 
        item(mixed):   Item used for the search within the list
    Returns:
        (Tuple): time in seconds
    """
    a_list.sort()
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    timecalc = end - start

    if not found:
        midpoint = -1

    return (midpoint, timecalc)


def binary_search_recursive(a_list, item):
    """This is a binary search recursive function.
    Args:
        a_list(list):  A list contenting positive integers 
        item(mixed):   Item used for the search within the list
    Returns:
        (Tuple): time in seconds
    """
    def binary_search_helper(a_list, item, start_time, start, end):
        if start > end:
            return (-1, time.time() - start)

        midpoint = (start + end) // 2

        if a_list[midpoint] == item:
            return (midpoint, time.time() - start)
        else:
            if item < a_list[midpoint]:
                return binary_search_helper(a_list, item, start_time, start,
                                            midpoint - 1)
            else:
                return binary_search_helper(a_list, item, start_time,
                                            midpoint + 1, end)

    a_list.sort()
    start = time.time()
    return binary_search_helper(a_list, item, start, 0, len(a_list))

def generate_random_list(total_lists, list_length):
    mylists = []
    for i in range(total_lists):
        a_list = range(list_length)
        random.shuffle(a_list)
        mylists.append(a_list)
    return mylists

def main():
    """The main function print how long each search function takes, on average
    with 100 random input list of positive integers of size 500, 1000, and
    10000, and taking the average run time of the 100 lists.
    """
    num_of_list = 100
    search_functions = [(sequential_search, "Sequential Search"),
                      (ordered_sequential_search, "Ordered Sequential Search"),
                      (binary_search_iterative, "Binary Search Iterative"),
                      (binary_search_recursive, "Binary Search Recursive")]
    test_list_size = [500, 1000, 10000]

    for list_size in test_list_size:

        sum_of_search_time_list = []

        for i in range(len(search_functions)):
            sum_of_search_time_list.append(0.0)

        print("List of size %d:"%(list_size))

        for i in range(num_of_list):

            a_list = generate_random_list(num_of_list, list_size)

            for x, function_tuple in enumerate(search_functions):
                function, name = function_tuple
                result, duration = function(a_list, -1)
                sum_of_search_time_list[x] += duration

        for x, function_tuple in enumerate(search_functions):
            function, name = function_tuple
            print("    %s took %10.7f seconds to run, on average"%(name,
                 (sum_of_search_time_list[x]/num_of_list)))

if __name__ == '__main__':
    main()
