# -*- coding: utf-8 -*-
from queue import Queue


class Node(object):
    def __init__(self, value):
        self.value = value
        self.connections = []

    def set_connections(self, to_node):
        if to_node not in self.connections:
            self.connections.append(to_node)


def parse_data_to_node(connection_list) -> dict:
    n_dict = {}
    for connection in connection_list:
        f_value, t_value = connection.split("-")
        if f_value in n_dict:
            f_node = n_dict[f_value]
        else:
            f_node = Node(f_value)
            n_dict[f_value] = f_node
        if t_value in n_dict:
            t_node = n_dict[t_value]
        else:
            t_node = Node(t_value)
            n_dict[t_value] = t_node

        if f_value == "start" or t_value == "end":
            f_node.set_connections(t_node)
        elif t_value == "start" or f_value == "end":
            t_node.set_connections(f_node)
        else:
            f_node.set_connections(t_node)
            t_node.set_connections(f_node)

    return n_dict


# part1
def get_all_traversal_paths_part1(node_dict):
    path_list = []
    queue = Queue()
    start_node = node_dict.get("start")
    queue.put(start_node.value)

    while not queue.empty():
        temp_path = queue.get()
        node_value_list = temp_path.split(",")
        node = node_dict.get(node_value_list[-1])
        for connection in node.connections:
            node_name = connection.value
            if node_name == "end":
                path_list.append("{},end".format(temp_path))
            elif node_name == node_name.lower():
                if node_name not in temp_path:
                    queue.put("{},{}".format(temp_path, node_name))
            else:
                queue.put("{},{}".format(temp_path, node_name))

    return path_list


# part2
def get_all_traversal_paths_part2(node_dict):
    path_list = []
    queue = Queue()
    start_node = node_dict.get("start")
    queue.put((start_node.value, True))

    while not queue.empty():
        temp_path, allow_lower_case_duplicated = queue.get()
        node_value_list = temp_path.split(",")
        node = node_dict.get(node_value_list[-1])
        for connection in node.connections:
            node_name = connection.value
            if node_name == "end":
                path_list.append("{},end".format(temp_path))
            elif node_name == node_name.lower():
                count = node_value_list.count(node_name)
                if count == 0:
                    queue.put(("{},{}".format(temp_path, node_name), allow_lower_case_duplicated))
                elif all([
                    count == 1,
                    # connection.value != "start",
                    allow_lower_case_duplicated
                ]):
                    queue.put(("{},{}".format(temp_path, node_name), False))
            else:
                queue.put(("{},{}".format(temp_path, node_name), allow_lower_case_duplicated))

    return path_list


if __name__ == "__main__":
    # read data
    with open("data/day12_input.txt") as f:
        data_list = f.readlines()
    caves_connection_list = [line.strip() for line in data_list]

    # parse data
    n_dict = parse_data_to_node(caves_connection_list)

    # traversal part1 and output
    print(len(set(get_all_traversal_paths_part1(n_dict))))

    # traversal part2 and output
    print(len(set(get_all_traversal_paths_part2(n_dict))))
