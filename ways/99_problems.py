import pandas as pd
from random import randint


def problem_maker(roads):
    path_list = []
    for i in range(1, 101):
        valid_path = True
        rand_index = randint(1, len(roads.junctions()))
        source_junction = roads.junctions()[rand_index]

        if len(source_junction.link) == 0:
            i -= 1
            continue

        source_junction_link = randint(0, len(source_junction.links - 1))
        path_len = randint(2, 11)
        target_junction = roads.junctions()[source_junction.links[source_junction_link].target]

        for j in range(1, path_len):
            target_junction_link = randint(0, len(target_junction.links) - 1)
            if len(target_junction.links) == 1:
                valid_path = False
                break
            else:
                target_junction = roads.junctions()[target_junction.links[target_junction_link].target]

        if not valid_path or source_junction.index == target_junction.index:
            i -= 1
            continue

        path_list.append([source_junction.index, target_junction.index])
        problems_list = pd.DataFrame(path_list)
        problems_list.to_csv('problems.csv')
    return path_list





