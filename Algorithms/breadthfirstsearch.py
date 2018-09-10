#!/usr/bin/env python3 

from collections import defaultdict

# Breadth First Search
# Uses the graph from ../DataStructures/graph.py
# Uses the queue from ../DataStructures/queue.py

# Includes Breadth First Paths (Shortest Path from source vertice to another based on edges (not weights))

# Operations

# path_to --> Returns the path from the source to the given vertice if one exists else returns None
# has_path_to --> Returns whether or not a path exists from the source to the given vertice. (True / False)

# Performance

# Dependent on graph structure.

# Comparisons

# Useful for searching for shortest path in terms of edges in unweighted graphs.

class BreadthFirstSearch(object):

    def __init__(self, graph, source):
        self.marked = defaultdict(bool)
        self.edge_to = defaultdict(list)
        self.source = source

        self.bfs(graph, source)

    def bfs(self, graph, source):
        q = Queue()
        self.marked[source] = True
        q.enqueue(source)
        while not q.is_empty():
            v = q.dequeue()
            for edge in graph.adj[v]:
                if not self.marked[edge]:
                    self.edge_to[edge] = v
                    self.marked[edge] = True
                    q.enqueue(edge)
        
    def has_path_to(self, vertice):
        return self.marked[vertice]
    
    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        #path acts as a stack in this instance - could import stack data type
        path = [v]
        x = v 
        while not(x == self.source):
            x = self.edge_to[x]
            path.append(x)
        return path[::-1]




# Dependent Data Structures

class Queue(object):

    def __init__(self):

        self.q = []
    
    def enqueue(self, s):
        self.q.append(s)
    
    def dequeue(self):
        item = self.q[0]
        self.q = self.q[1:]
        return item
    
    def __len__(self):
        return len(self.q)
    
    def first(self):
        return self.q[0]
    
    def is_empty(self):
        return len(self.q) == 0 

class Graph(object):

    def __init__(self, directed=False):
        self.E = 0
        self.V = 0
        self.directed = directed
        self.adj = defaultdict(list)
        self.inverted_index = []
        self.symbol_table = {}

    
    def add_edge(self, v1, v2):
        if v1 not in self.symbol_table.keys():
            self.symbol_table[v1] = self.V
            self.inverted_index.append(v1)
            self.V += 1
        if v2 not in self.symbol_table.keys():
            self.symbol_table[v2] = self.V
            self.inverted_index.append(v2)
            self.V += 1
        
        self.adj[self.symbol_table[v1]].append(self.symbol_table[v2])
        self.E += 1 
        if not self.directed:
            self.adj[self.symbol_table[v2]].append(self.symbol_table[v1])
            self.E += 1

    
    def __str__(self):
        text = ""
        for key in self.adj.keys():
            text += str(key)+" : "+str(self.adj[key])+"\n"
        return text

#Simple Test
def main():
    q = Graph()
    q.add_edge(1, 4)
    q.add_edge(4, 5)
    q.add_edge(5, 6)
    q.add_edge(6, 2)
    q.add_edge(2, 3)
    q.add_edge(1, 2)
    bfs = BreadthFirstSearch(q, 0)
    print(str(bfs.path_to(3)))


if __name__ == '__main__':
    main()

        

