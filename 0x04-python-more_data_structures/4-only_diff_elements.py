#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uncommon_set1 = set_1.difference(set_2)
    uncommon_set2 = set_2.difference(set_1)
    return uncommon_set1.union(uncommon_set2)
