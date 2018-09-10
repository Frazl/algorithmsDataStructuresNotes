#!/usr/bin/env python3 

# Uses for queues involve anything where you want things to happen in the order that they were called, but whatever is processing the queue can't keep up to speed.
# A good use case example of a queue in computing is when typing on an old computer quickly.
# The computer can't handle all the keystrokes and therefore queues them up to be displayed.


# Operations

# The queue supports: enqueue, dequeue, first, is_empty. These are all fairly obvious as what they do. 

# Performance

# All operations are O(1)


# Comparisons

# A queue is first in first out (FIFO) where as stack is last in first out (LIFO). Therefore a Queue and stack have different use cases. 
 

class Queue(object):

    def __init__(self):

        self.q = []
    
    def enqueue(self, s):
        self.q.append(s)
    
    def dequeue(self):
        item = self.q[0]
        self.q = self.q[1:]
        return item
    
    def __len__(self):
        return len(self.q)
    
    def first(self):
        return self.q[0]
    
    def is_empty(self):
        return len(self.q) == 0 