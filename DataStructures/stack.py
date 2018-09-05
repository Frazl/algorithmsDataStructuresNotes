#!/usr/bin/env python3 

# Stacks are often described by analogy to a spring-loaded stack of plates in a cafeteria. 
# Clean plates are placed on top of the stack, pushing down any already there. 
# When a plate is removed from the stack, the one below it pops up to become the new top.


# Operations

# The queue supports: push, pop, top, is_empty. 
# push - appends to the top of the stack
# pop - removes and returns whatever is on top of stack.


# Performance

# Most operations are O(1)
# Displaying the length is O(1)
# Displaying whether or not is_empty is O(n)

# Comparisons

# A Stack is last in first out (LIFO) and is similar to a queue.




class Stack(object):

    def __init__(self):

        self.stack = []

    def push(self, n):
        self.stack.append(n)
    
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def __len__(self):
        return len(self.stack)
    
    def is_empty(self):
        if len(self.stack):
            return False
        else:
            return True
    
