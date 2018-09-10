#!/usr/bin/env python3 

from collections import defaultdict

# Simple Graph class. This uses the adjaceny lists variation of a graph. 
# This graph uses a symbol table to limit memory usage. e.g. Instead of storing possibly large strings we record the value and link it to an number in a list.
# The alternative version of a graph is an adjacency matricies.
# This graph does not account for weights


# Operations

# add_edge - Add's an edge from one vertice to another, if directed is False then it adds an edge in the opposite direction too. i.e. Accounts for both directed and undirected graphs.


# Performance

# Space - E + V 
# add edge - 1 
# check whether w is adjacent to v - length of adjacent list of v (i.e. degree(v))
# iterate through vertices adjacent to v - length of adjacent list of (i.e. degree(v))

# Comparisons

# Similar to a matrices graph but with different performance. 
# This uses less Space (memory) for sparse graphs compared to matrices graphs
# Higher performance requirements for checking adjacency given source and other vertice
# Higher performance requirements for iterating through vertices adjacent to a given vertice

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
    q.add_edge('Hello', 'World')
    q.add_edge('World', 'Sean')
    q.add_edge('End', 'Near')
    q.add_edge('World', 'Peace')
    print(q)


if __name__ == '__main__':
    main()

        

