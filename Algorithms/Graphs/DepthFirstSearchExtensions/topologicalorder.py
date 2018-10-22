#!/usr/bin/env python3

from collections import defaultdict

class TopologicalSort(object):

    def __init__(self, graph):
        self.order = None
        self.cyclefinder = DirectedCycle(graph)
        if not self.cyclefinder.has_cycle():
            self.depth_first_order = DepthFirstOrder(graph)
            self.order = self.depth_first_order.reversePost
        

    def isDAG(self):
        return self.order == None
    

        





class DepthFirstOrder(object):
    
    def __init__(self, graph):
        self.reversePost = Stack()
        self.marked = [False] * graph.V
        
        s = 0 
        while s < graph.V:
            if not self.marked[s]:
                self.dfs(graph, s)
            s += 1
        
    def dfs(self, graph, s):
        self.marked[s] = True
        for vertex in graph.adj[s]:
            if not self.marked[vertex]:
                self.dfs(graph, vertex)
        self.reversePost.push(s)




class DirectedCycle(object):

    def __init__(self, graph):

        self.marked = [False] * graph.V
        self.edge_to = defaultdict(list)
        self.on_stack = [False] * graph.V 
        self.count = 0
        self.graph = graph
        self.cycle = None
        v = 0 
        while v < graph.V:
            if not self.marked[v]:
                self.dfs(v)
            v += 1
        
    def dfs(self, search_query):
        self.marked[search_query] = True
        self.on_stack[search_query] = True
        self.count += 1
        for value in self.graph.adj[search_query]:
            if self.has_cycle():
                return
            elif not self.marked[value]:
                self.edge_to[value] = search_query
                self.dfs(value)
            elif self.on_stack[value]:
                self.cycle = Stack()
                x = search_query
                while x != value:
                    self.cycle.push(x)
                    x = self.edge_to[x]
                self.cycle.push(value)
                self.cycle.push(search_query)
        self.on_stack[search_query] = False

    def has_cycle(self):
        return self.cycle != None
    
# Required Data Structures

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

# Required Stack

class Stack(object):

    def __init__(self):

        self.stack = []

    def push(self, n):
        self.stack.append(n)
    
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def __len__(self):
        return len(self.stack)
    
    def is_empty(self):
        if len(self.stack):
            return False
        else:
            return True



def main():
    q = Graph(directed=True)
    q.add_edge('Algorithms', 5)
    q.add_edge('Algorithms', 1)
    q.add_edge('Algorithms', 6)
    q.add_edge(2, 'Algorithms')
    q.add_edge(2, 3)
    q.add_edge(3, 5)
    q.add_edge(5, 4)
    q.add_edge(6, 4)
    q.add_edge(6, 9)
    q.add_edge(7, 6)
    q.add_edge(8, 7)
    q.add_edge(9, 10)
    q.add_edge(9, 11)
    q.add_edge(9, 12)
    q.add_edge(11, 12)
    c = TopologicalSort(q)
    s = c.order
    while not s.is_empty():
        print(q.inverted_index[s.pop()])

if __name__ == '__main__':
    main()