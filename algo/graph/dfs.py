from algo.graph.graph import Graph


def dfs(graph, start):
    visited = {}
    res = []

    def dfs_recursive(vertex):
        visited[vertex] = True
        res.append(str(vertex))
        adj_node = graph.graph[vertex]
        while adj_node:
            if adj_node.vertex not in visited:
                dfs_recursive(adj_node.vertex)
            adj_node = adj_node.next

    dfs_recursive(start)

    return "".join(res)


def dfs_iterative(graph, start):
    visited = set()
    res = ""
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            res += str(vertex)
        adj_node = graph.graph[vertex]
        while adj_node:
            if adj_node.vertex not in visited:
                stack.append(adj_node.vertex)
            adj_node = adj_node.next
    return res


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    print(dfs_iterative(g, 0))
