class Graph:
    def __init__(self):
        self.dic = {}
    
    def add_vertex(self, data):
        #saving the vertex as key and value as empty list
        self.dic[data] = []

    def insert(self, vertex, edge, is_bidirectional):
        #if the key is not present...
        #adding the key only
        if vertex not in self.dic:
            self.add_vertex(vertex)
        
        #if there is no edge in the dic
        #first create a key for that edge 
        if edge not in self.dic:
            self.add_vertex(edge)
        #then add this edge as value of the current vertex
        self.dic[vertex].append(edge)
    
        if is_bidirectional:
            #add the vertex as value of the current edge
            self.dic[edge].append(vertex)


    def display(self):
        for x in self.dic:
            print(f"{x}: {' '. join(map(str, self.dic[x]))}")


graph = Graph()
graph.insert(4,5,True)
graph.insert(4,56,True)
graph.insert(5,7,False)
graph.display()
