#GRAPH
#IndexDic, ValList, Directed, 

#DFS
#MARKED, EDGE_TO, SOURCE, GRAPH

from collections import defaultdict

class Graph(object):

    def __init__(self, directed=False):
        
        self.directed = directed
        
        self.vl = []
        self.id = {}
        self.adj = defaultdict(set)
        self.V = 0
        self.E = 0

    def add_edge(self, v1, v2):
        if v1 not in self.id.keys():
            self.vl.append(v1)
            self.id[v1] = self.V
            self.V += 1
        if v2 not in self.id.keys():
            self.vl.append(v2)
            self.id[v2] = self.V
            self.V += 1 


        self.adj[self.id[v1]].add(self.id[v2])
        if not self.directed:
            self.adj[self.id[v2]].add(self.id[v1])
        
    def remove_edge(self, v1, v2):
        self.adj[self.id[v1]].remove(self.id[v2])
        if not self.directed:
            self.adj[self.id[v2]].remove(self.id[v1])
    
    def __str__(self):
        s = ""
        for key in self.adj:
            s += str(self.vl[key]) + "| "
            for val in self.adj[key]:
                s += str(self.vl[val]) + " "
            s += "\n"
        return s

class DFS(object):
    
    def __init__(self, graph, source=0):

        self.marked = defaultdict(bool)
        self.edge_to = {}
        self.count = 0 

        self.graph = graph
        self.source = source
        self.dfs(self.graph, self.source)

    def dfs(self, graph, source):
        self.marked[source] = True
        for x in graph.adj[source]:
            if not self.marked[x]:
                self.edge_to[x] = source
                self.dfs(graph, x)

    def has_path_to(self, x):
        return self.marked[x]

    def path_to(self, x):
        if not self.has_path_to(x):
            return []
        else:
            l = []
            k = x 
            while k != self.source:
                l.append(self.graph.vl[k])
                k = self.edge_to[k]
            return l[::-1]


class Queue(object):

    def __init__(self):

        self.q = []

    def enqueue(self, item):

        self.q.append(item)

    def dequeue(self):

        item = self.q[0]
        del(self.q[0])
        return item

    def is_empty(self):
        return len(self.q) == 0

class BFS(object):

    def __init__(self, graph, source=0):

        self.graph = graph
        self.source = source

        self.marked = defaultdict(bool)
        self.edge_to = defaultdict(list)

        self.BFS(self.graph, self.source)

    def BFS(self, graph, source):
        q = Queue()
        self.marked[source] = True
        q.enqueue(source)
        while q.is_empty() == False:
            v = q.dequeue()
            for e in graph.adj[v]:
                if not self.marked[e]:
                    self.edge_to[e] = v
                    self.marked[e] = True
                    self.BFS(graph, e)
    
    def has_path_to(self, item):
        return self.marked[item]

    def path_to(self, item):
        if not self.has_path_to(item):
            return None
        l = []
        k = item
        while self.source != k:
            l.append(self.graph.vl[k])
            k = self.edge_to[k]
        return l[::-1]


def merge(left, right):
    i = j = 0 
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1 
        else:
            result.append(right[j])
            j += 1 
    
    result += left[i:]
    result += right[j:]

    return result 

def merge_sort(a):
    
    if len(a) <= 1:
        return a 
    
    middle = len(a) // 2 
    left = a[:middle]
    right = a[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

a = [5,126,1,67,612,521,67,3,512,6734,723,412,6234,73,523,634,7345,3245]
print(merge_sort(a))