class AdjNode:

    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, source, destination):
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


class UndirectedGraph(Graph):
    def add_edge(self, source, destination):
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        node = AdjNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    g.print_graph()
