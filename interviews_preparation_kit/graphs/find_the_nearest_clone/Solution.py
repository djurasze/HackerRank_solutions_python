#!/bin/python3


class Node:
    def __init__(self, id, color):
        self.id = id
        self.color = color
        self.neighbours = []
        self.visited = False

    def add_neighbour(self, node):
        self.neighbours.append(node)

    def mark_as_visited(self):
        self.visited = True

    def __repr__(self):
        return "(id: %s, color: %s, neighbours: %s)" % (
        self.id, self.color, list(map(lambda node: node.id, self.neighbours)))


class Graph:
    def __init__(self, ids, graph_from, graph_to):
        self.nodes = {ind + 1: Node(ind + 1, color) for (ind, color) in enumerate(ids)}
        [self.add_edge(id_from, id_to) for id_from, id_to in zip(graph_from, graph_to)]

    def add_edge(self, id_from, id_to):
        from_node = self.nodes[id_from]
        to_node = self.nodes[id_to]
        from_node.add_neighbour(to_node)
        to_node.add_neighbour(from_node)

    def get_all_of_color(self, color):
        return list(map(lambda data: data[0], filter(lambda data: data[1].color == color, self.nodes.items())))

    def reset_visited(self):
        for node in self.nodes.values():
            node.visited = False

    def find_shortest_path_between(self, id_from, id_to):
        start = self.nodes[id_from]
        result = self.find_shortest_path_next_step(start, id_to)
        self.reset_visited()
        return result -1

    def find_shortest_path_next_step(self, current, id_to):
        if current.id == id_to:
            return 1

        not_visited_neighbours = list(filter(lambda node: node.visited is False, current.neighbours))
        if len(not_visited_neighbours) == 0:
            return 999

        current.visited = True
        min_path = 999
        for next in not_visited_neighbours:
            path = self.find_shortest_path_next_step(next, id_to)
            if path < min_path:
                min_path = path
        current.visited = False
        return min_path + 1

    def remove_node(self, id):
        neighbours = self.nodes.get(id).neighbours
        [node.neighbours.remove(self.nodes[id]) for node in neighbours]
        del self.nodes[id]


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = Graph(ids, graph_from, graph_to)
    same_color_node_ids = graph.get_all_of_color(val)

    # print(graph.nodes)
    # print(same_color_node_ids)
    result = graph_nodes + 1
    while len(same_color_node_ids) != 0:
        from_id = same_color_node_ids[0]
        for to_id in same_color_node_ids[1:]:
            shortest_path = graph.find_shortest_path_between(from_id, to_id)
            if shortest_path < result:
                result = shortest_path
        same_color_node_ids = same_color_node_ids[1:]
        graph.remove_node(from_id)

    # print(graph.nodes)

    return -1 if result == graph_nodes + 1 else result


if __name__ == '__main__':
    f = open("data.txt", "r")

    graph_nodes, graph_edges = map(int, f.readline().strip().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, f.readline().strip().split())

    ids = list(map(int, f.readline().strip().split()))

    val = int(f.readline().strip())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    print(ans)

    f.close()
