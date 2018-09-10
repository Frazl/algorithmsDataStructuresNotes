#!/usr/bin/env python3 

from collections import defaultdict
# Connected Components - Uses Depth First Search to divide the vertices of a graph into equivalence classes 
# i.e. If the vertices of a graph aren't all linked this will show what sections are linked.   
# uses the Graph class (same as within ../../datastructures/graph.py)

class CC(object):

    def __init__(self, graph):

        self.marked = defaultdict(bool)
        self.id = [None] * graph.V
        self.count = 0
        self.graph = graph
        s = 0 
        while s < self.graph.V:
            if not self.marked[s]:
                self.dfs(s)
                self.count += 1
            s += 1
        
    def dfs(self, search_query):
        self.marked[search_query] = True
        #This line below is the only change to the DFS found in ./depthfirstsearch.py
        self.id[search_query] = self.count
        for value in self.graph.adj[search_query]:
            if not self.marked[value]:
                self.dfs(value)
    
    def identify(self, v):
        return self.id[v]

    def connected(self, v, w):
        return self.id[v] == self.id[w]
    
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


def main():
    q = Graph()
    q.add_edge(5, 6)
    q.add_edge(1, 2)
    q.add_edge(4, 5)
    q.add_edge(7, 'Hello')
    q.add_edge(2, 3)
    c = CC(q)
    print(c.identify(q.symbol_table[1]))
    print(c.identify(q.symbol_table[2]))
    print(c.identify(q.symbol_table[4]))
    print(c.identify(q.symbol_table[5]))
    print(c.identify(q.symbol_table['Hello']))
    print(c.connected(q.symbol_table[7], q.symbol_table['Hello']))

if __name__ == '__main__':
    main()