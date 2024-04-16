class Graph:
    def __init__(self):
        self.dic = {}

    def add_vertex(self, data):
        self.dic[data] = []


    def insert(self, vertex, edge, is_bidirectional):
        if vertex not in self.dic:
            self.add_vertex(vertex)
        if edge not in self.dic:
            self.add_vertex(edge)
        self.dic[vertex].append(edge)
        if is_bidirectional:
            self.dic[edge].append(vertex)

    def display(self):
        for x in self.dic:
            print(f"{x}: {' '.join(map(str, self.dic[x]))}")


graph = Graph()
graph.insert(3, 5, True)
graph.insert(3, 4, True)
graph.insert(5, 6, False)
graph.display()