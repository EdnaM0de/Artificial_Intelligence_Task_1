'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''
import collections
from collections import namedtuple
from ways import load_map_from_csv
import math
from ways.info import ROAD_TYPES


def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    junction_number = junction_count(roads)
    link_number = link_count(roads)

    return {
        'Number of junctions' : junction_number,
        'Number of links' : link_number,
        'Outgoing branching factor' : Stat(max=max_branch(roads), min=min_branch(roads), avg=average_branch(roads)),
        'Link distance' : Stat(max=max_link(roads), min=min_link(roads), avg=average_links(roads)),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram' : link_type_histogram(roads),  # tip: use collections.Counter
    }


def junction_count(roads):
    # Statistic: number of junctions.
    count = 0
    for junction in roads.junctions():
        count += 1
    return count


def link_count(roads):
    # Statistic: number of links.
    count = 0
    for link in roads.iterlinks():
        count += 1
    return count


def max_branch(roads):
    # Statistic: maximum branch factor of a junction.
    max_factor = 0
    for junction in roads.junctions():
        if len(junction[3]) > max_factor:
            max_factor = len(junction[3])
    return max_factor


def min_branch(roads):
    # Statistic: minimum branch factor of a junction.
    min_factor = math.inf
    for junction in roads.junctions():
        if len(junction[3]) < min_factor:
            min_factor = len(junction[3])
    return min_factor


def average_branch(roads):
    # Statistic: average branch factor of all junctions.
    add = 0
    for junction in roads.junctions():
        add += len(junction[3])
    avg = add / junction_count(roads)
    return avg


def max_link(roads):
    # Statistic: maximum number of links per junction.
    max_factor = 0
    for link in roads.iterlinks():
        if link[2] > max_factor:
            max_factor = link[2]
    return max_factor


def min_link(roads):
    # Statistic: minimum number of links per junction.
    min_factor = math.inf
    for link in roads.iterlinks():
        if link[2] < min_factor:
            min_factor = link[2]
    return min_factor


def average_links(roads):
    # Statistic: average distance of all links.
    add = 0
    for link in roads.iterlinks():
        add += link[2]
    avg = add / link_count(roads)
    return avg


def link_type_histogram(roads):
    # Statistic: histogram of different road types, meaning the count of each type.
    link_type = []
    for link in roads.iterlinks():
        link_type.append(ROAD_TYPES[link.highway_type])
    return collections.Counter(link_type)


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))

        
if __name__ == '__main__':
    from sys import argv
    assert len(argv) == 1
    print_stats()

