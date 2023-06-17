from algo.graph.dfs import dfs
from algo.graph.graph import Graph
from algo.graph.transpose import transpose


def is_strongly_connected(graph):
    """
    Finds if the graph is strongly connected or not
    :param graph: The graph
    :return: returns True if the graph is strongly connected, otherwise False
    """
    return len(dfs(graph, 0)) == graph.V and len(dfs(transpose(graph), 0)) == graph.V


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 0)
    g.add_edge(4, 2)
    print(is_strongly_connected(g))
