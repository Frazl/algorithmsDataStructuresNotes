#!/usr/bin/env python3 

from collections import defaultdict
# Cycle Detection - Detects if there is a directred cycle. Can only be used with directed graphs...
# uses the Graph class (same as within ../../datastructures/graph.py)

class DirectedCycle(object):

    def __init__(self, graph):

        self.marked = [False] * graph.V
        self.edge_to = defaultdict(list)
        self.on_stack = [False] * graph.V 
        self.count = 0
        self.graph = graph
        self.cycle = None
        for v in range(graph.V):
            if not self.marked[v]:
                self.dfs(v)
        
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
    q.add_edge(0, 5)
    q.add_edge(5, 4)
    q.add_edge(4, 3)
    q.add_edge(3, 5)
    dc = DirectedCycle(q)
    print(dc.has_cycle())
    while len(dc.cycle) != 0:
        print(dc.cycle.pop())

if __name__ == '__main__':
    main()