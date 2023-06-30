#!/usr/bin/python3
''' a function that finds a peak in a list of unsorted integers '''


def find_peak(list_of_integers):
    '''
    find the peak of the numbers
    list_of_integers : list of numbers
    '''

    # left and right pointrs
    left = 0
    right = len(list_of_integers) - 1

    if len(list_of_integers) == 0:
        return None
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
