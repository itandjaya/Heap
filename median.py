# median.py
from heap_queue import *;

class Median:
    
    def __init__ (self, data = []):
        
        self.min_heap, self.max_heap = MinHeap(), MaxHeap();
        
        for n in data:
            self.add_value(n);
        
        return;
    
    def add_value(self, x):
        
        self.max_heap.heappush(x);            
        self.rebalance_heap();
        
        #print(self.max_heap.data, self.min_heap.data);
        
        return self.median();
    
    def rebalance_heap(self):
        
        ## rebalances the heap sizes.
        while (self.max_heap.sizeof() > self.min_heap.sizeof() + 1):
            
            self.min_heap.heappush(    self.max_heap.heappop()    );
        
        
        
        #rebalances max and min heap top values.
        while    self.max_heap.sizeof() and self.min_heap.sizeof() and \
                 self.max_heap.heap_top() > self.min_heap.heap_top():
            
            max_top, min_top = self.max_heap.heappop(), self.min_heap.heappop();
            self.max_heap.heappush(min_top);
            self.min_heap.heappush(max_top);
            

            #self.max_heap.data[0], self.min_heap.data[0] = \
            #self.min_heap.data[0], self.max_heap.data[0]
            
            #self.min_heap.move_down(0);
            
        return;
    
    def median(self):
        
        max_size, min_size = self.min_heap.sizeof(), self.max_heap.sizeof();
        
        if (min_size + max_size) & 1:
            return self.max_heap.heap_top()*1.0;
        
        else:
            return (self.max_heap.heap_top() + self.min_heap.heap_top()) / 2.0;