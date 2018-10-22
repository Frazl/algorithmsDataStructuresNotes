import random


class Quicksort(object):
    
    def __init__(self, a):
        self.a = a
        print('---')
        print(self.a)
        print('---')
        # The implementation of random.shuffle() uses the Fisher-Yates shuffle algorithm, which is easily seen to be O(n).
        random.shuffle(self.a)
        self.q_sort(0, len(self.a) - 1)
       
    def q_sort(self, lo, hi):
        if lo < hi:
            pivot_index = (lo + hi) // 2
            print(self.a, lo, hi, pivot_index)
            pivot_new_index = self.partition(pivot_index, lo, hi)
            self.q_sort(lo, pivot_new_index - 1)
            self.q_sort(pivot_new_index + 1, hi)
            

    def partition(self, pivot_index, lo, hi):
        
        pivot = self.a[pivot_index]
        self.swap(pivot_index, hi)
        store_index = lo
        i = lo 
        for x in self.a[lo:hi]:
            if x < pivot:
                self.swap(i, store_index)
                store_index += 1
            i += 1 
        self.swap(store_index, hi)
        return store_index

    def swap(self, i, j):
            tmp = self.a[i]
            self.a[i] = self.a[j]
            self.a[j] = tmp






sortedList = Quicksort([6, 8, 4, 3 , 2 , 10, 1, 9, 0, 5, 7])
print(sortedList.a)