#!/usr/bin/env python3 

from collections import defaultdict

# Simple Graph class. This uses the adjaceny lists variation of a graph. 
# The alternative version of a graph is an adjacency matricies.  


# Operations

# 


# Performance

# 

# Comparisons

# 

class Graph(object):

    def __init__(self, directed=False):
        self.V = 0
        self.E = 0
        self.directed = directed
        self.adj = defaultdict(list)

    
    def add_edge(self, v1, v2):
        self.adj[v1].append(v2)
        if not self.directed:
            self.adj[v2].append(v1)
        self.E += 1
    
    def __str__(self):
        text = ""
        for key in self.adj.keys():
            text += str(key)+" : "+str(self.adj[key])+"\n"
        return text

#Simple Test
def main():
    q = Graph()
    q.add_edge(3, 4)
    q.add_edge(4, 5)
    q.add_edge(5, 3)
    print(q)


if __name__ == '__main__':
    main()

        

