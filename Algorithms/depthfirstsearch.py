#!/usr/bin/env python3 

from collections import defaultdict
# Depth First Search using the Graph class (same as within ../datastructures/graph.py)


# Operations

# 


# Performance

# 

# Comparisons

# 

class DepthFirthSearch(object):

    def __init__(self, graph, search_query):

        self.marked = defaultdict(bool)
        self.count = 0
        self.graph = graph
        self.dfs(search_query)

    def dfs(self, search_query):
        self.marked[search_query] = True
        self.count += 1
        for value in self.graph.adj[search_query]:
            if not self.marked[value]:
                self.dfs(value)
    
    def __str__(self):
        text = ""
        for key in self.marked:
            text += str(key)+' : '+str(self.marked[key])+'\n'
        return text

# Depth First Paths - Finds a path using depth first search

class DepthFirstPaths(object):

    def __init__(self, graph, source):
        
        self.marked = defaultdict(bool)
        self.edge_to = defaultdict(list)
        self.source = source
        self.graph = graph
        self.dfs(source)

    def dfs(self, search_query):
        self.marked[search_query] = True
        for value in self.graph.adj[search_query]:
            if not self.marked[value]:
                self.edge_to[value] = search_query
                self.dfs(value)

    def has_path_to(self, v):
        return self.marked[v]
    
    def pathTo(self, v):
        if not self.has_path_to(v):
            return None
        #path acts as a stack in this instance - could import stack data type
        path = [v]
        x = v 
        while not(x == self.source):
            x = self.edge_to[x]
            path.append(x)
        return path[::-1]




#Graph Datastructure is required an no clean way to import from neutral directories
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

#Test Cases

def main():
    q = Graph(True)
    q.add_edge(0, 2)
    q.add_edge(2, 1)
    q.add_edge(2, 3)
    q.add_edge(3, 4)
    q.add_edge(3, 5)
    q.add_edge(6, 5)

    print(q)
    #Depth First Search Tests
    n = 2
    dfs = DepthFirthSearch(q, n)
    print('There is a path from '+str(n)+' to:')
    print(dfs)
    
    #Depth First Path Test
    path_from = 0 
    path_to = 5
    
    path = DepthFirstPaths(q, path_from)
    
    print('The path from '+str(path_from)+' to '+str(path_to))

    a = []
    for x in path.pathTo(5):
        a.append(str(x))
    print('-'.join(a))

    checkPath = 2 
    print('The statement: There is a path to '+str(checkPath)+' from '+str(path_from)+' is '+str(path.has_path_to(checkPath)))
        


if __name__ == '__main__':
    main()