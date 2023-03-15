#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score = max(list(a_dictionary.values()))
        for i in a_dictionary.keys():
            if a_dictionary[i] == best_score:
                return i
