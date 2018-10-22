class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        if self.root == None:
            self.root = Node(item, None, None) 
        else:
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item:
                    child_tree = child_tree.left 
                else:
                    child_tree = child_tree.right

            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)
                
    def recursive_count(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.recursive_count(ptr.right) +  self.recursive_count(ptr.left)
            
                
    def count(self):
        return self.recursive_count(self.root)


def main():
    bt = BST()
    bt.add(9)
    bt.add(5)
    bt.add(20)
    bt.add(2)
    bt.add(3)
    bt.add(91)
    bt.add(251)
    bt.add(2541)
    print(bt.count())

if __name__ == '__main__':
    main()