import copy

from algo.graph.graph import Graph


def find_all_paths(graph, source, destination):
    result = []

    def find_all_paths_util(src, dest, visited, path):
        visited.add(src)
        path.append(src)

        if src == dest:
            result.append(copy.deepcopy(path))
        else:
            adj_node = graph.graph[src]
            while adj_node:
                adj_vertex = adj_node.vertex
                if adj_vertex not in visited:
                    find_all_paths_util(adj_vertex, dest, visited, path)

                adj_node = adj_node.next

        path.pop()
        visited.remove(src)

    find_all_paths_util(source, destination, visited=set(), path=[])
    return result


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    print(find_all_paths(g, 0, 5))
