from algo.graph.graph import Graph


def bfs(graph, start):
    visited, queue = {start}, [start]
    result = ""
    while queue:
        vertex = queue.pop(0)
        result += str(vertex)
        adj_node = graph.graph[vertex]
        while adj_node is not None:
            if adj_node.vertex not in visited:
                visited.add(adj_node.vertex)
                queue.append(adj_node.vertex)
            adj_node = adj_node.next
    return result


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    print(bfs(g, 0))
