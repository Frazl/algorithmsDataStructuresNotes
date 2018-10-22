class Node(object):

    def __init__(self, item):

        self.next = None
        self.item = item


class Linkedlist(object):

    def __init__(self):

        self.root = None
    
    def add(self, item):

        if self.root == None:
            self.root = Node(item)
        
        else:
            new = Node(item)
            new.next = self.root 
            self.root = new 
    
    def __iter__(self):
        ptr = self.root
        while ptr != None:
            yield ptr.item
            ptr = ptr.next