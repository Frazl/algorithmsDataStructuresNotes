from collections import defaultdict

class Graph(object):

    def __init__(self, directed=False):

        self.directed = directed
        self.V = 0
        self.E = 0 
        self.symbolTable = {}
        self.indexTable = []
        self.adj = defaultdict(list)

    def add_edge(self, v1, v2):
        if v1 not in self.symbolTable.keys():
            self.symbolTable[v1] = self.V
            self.indexTable.append(v1)
            self.V += 1
        if v2 not in self.symbolTable.keys():
            self.symbolTable[v2] = self.V
            self.indexTable.append(v2)
            self.V += 1
        self.adj[self.symbolTable[v1]].append(self.symbolTable[v2])
        if not self.directed:
            self.adj[self.symbolTable[v2]].append(self.symbolTable[v1])
    
    def __str__(self):
        text = ""
        for i in range (self.V):
            text += str(i) + ' ' + str(self.adj[i]) + '\n'
        return text

def main():
    g = Graph()
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    g.add_edge(9, 'Hello')
    print(g)

    

if __name__ == '__main__':
    main()