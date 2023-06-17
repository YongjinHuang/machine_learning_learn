from algo.graph.graph import Graph


def number_of_nodes(graph, level, root_vertex=0):
    queue = [(root_vertex, 1)]
    visited = {root_vertex}
    count = 0
    while queue:
        vertex, cur_level = queue.pop()
        if cur_level == level:
            count += 1

        adj_node = graph.graph[vertex]
        while adj_node:
            if adj_node.vertex not in visited:
                visited.add(adj_node.vertex)
                queue.append((adj_node.vertex, cur_level + 1))
            adj_node = adj_node.next
    return count


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    print(number_of_nodes(g, 4))
