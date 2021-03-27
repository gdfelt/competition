


class Day07(object):
    def __init__(self):
        graph = {}
        with open('advent_2020/day_07/day_07.dat') as file:
            for line in file:
                node, ver_list = line.strip().split(" contain ")
                node = node[:node.rfind(" ")]
                ver_list = ver_list.split(',')

                ver_list = [v[v.find(" ")+1:v.rfind(" ")].strip() for v in ver_list]

                print(ver_list)
                # I don't believe there any duplicates
                graph[node] = ver_list

    def part_01(self):
        return 0

    def part_02(self):
        return 0