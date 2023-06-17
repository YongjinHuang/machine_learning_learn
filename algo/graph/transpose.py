from algo.graph.graph import Graph


def transpose(graph):
    new_graph = Graph(graph.V)
    for i in range(graph.V):
        adj_node = graph.graph[i]
        while adj_node:
            new_graph.add_edge(adj_node.vertex, i)
            adj_node = adj_node.next

    return new_graph


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    gt = transpose(g)
    gt.print_graph()
