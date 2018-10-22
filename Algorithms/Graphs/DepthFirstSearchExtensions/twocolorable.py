#!/usr/bin/env python3

from collections import defaultdict


class TwoColor(object):

    def __init__(self, graph):
        self.marked = [False] * graph.V
        self.color = [False] * graph.V
        self.graph = graph
        self.is_two_colorable = True
        s = 0 
        while s < self.graph.V:
            if not self.marked[s]:
                self.dfs(s)
            s += 1
    def dfs(self, search_query):
        self.marked[search_query] = True
        for value in self.graph.adj[search_query]:
            if not self.marked[value]:
                self.color[value] = not self.color[search_query]
                self.dfs(value)
            elif self.color[value] == self.color[search_query]:
                self.is_two_colorable = False
    
    def is_bi_partite(self):
        return self.is_two_colorable
        

#Graph Datastructure is required an no clean way to import from neutral directories
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
    q.add_edge(5, 4)
    q.add_edge(4, 6)
    q.add_edge(6, 7)
    c = TwoColor(q)
    print(c.is_bi_partite())

if __name__ == '__main__':
    main()