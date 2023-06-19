from algo.graph.graph import Graph


def detect_cycle(graph):
    """
    Detects a cycle in a given graph
    :param graph: The graph
    :return: True if there is a cycle in the given graph, otherwise False
    """
    visited = set()
    cur_path = set()

    def detect_cycle_recursive(vertex):
        visited.add(vertex)
        cur_path.add(vertex)

        adj_node = graph.graph[vertex]
        while adj_node:
            adj_vertex = adj_node.vertex
            if adj_vertex not in visited:
                if detect_cycle_recursive(adj_vertex):
                    return True
            elif adj_vertex in cur_path:
                return True
            adj_node = adj_node.next

        cur_path.remove(vertex)
        return False

    for v in range(graph.V):
        if detect_cycle_recursive(v):
            return True
    return False


if __name__ == "__main__":
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    print(detect_cycle(g))
