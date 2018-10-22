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
    
    def __str__(self):
        s = ""
        for x in self:
            s += str(x) + " "
        return s

    def __iter__(self):
        ptr = self.root
        while ptr != None:
            yield ptr.item
            ptr = ptr.next

class Hashset(object):

    def __init__(self):

        self.table = [None] * 10
    
    def add(self, item):
        hash_value = hash(item)
        index = hash_value % len(self.table)
        if self.table[index] == None:
            self.table[index] = Linkedlist()
        if item not in self.table[index]:
            self.table[index].add(item)
        print(self.table[index])
    
    def contains(self, item):
        hash_value = hash(item)
        index = hash_value % len(self.table)
        if self.table[index] == None:
            return False
        if item not in self.table[index]:
            return False
        return True
    


h = Hashset()
h.add(31)
h.add(1)
h.add(4)
h.add(9)
h.add(35)
print(h.contains(32))