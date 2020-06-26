## heap_queue.py
## Implementation of heap classes: MinHeap and MaxHeap.
## The class creates a copy of input list, and heapify it.
## Original input list is not modified (for read-only).

## Input:   list ( int's, float's, char's)
## 2 methods to add data:
##  1. Passing a list in object declaration. Or,
##  2. Adding each element into the heap by using heappush( val).




class MinHeap:

    def __init__(self, list_input = []):
        ## Constructor of MinHeap. Takes list as input, then heapify it.
        ## Retuns None.    

        self.data   =   list_input;
        self.heapify();

        return;
    
    def heapify(self):
        # Using heappush() to populate the heap list.
        # Returns None.

        temp = self.data.copy();
        self.data = [];

        for n in temp:
            self.heappush(n);
        
        #print("HEAP: ", self.data);
        return;        

    def sorted(self):
        ## Returns a copy of sorted heap list.
        ## This function doesn't modify the heap list/structure.

        ans = [];
        temp = self.data.copy();        # Create duplicate copy of heaplist, for restoration later.

        while self.data:
            ans.append( self.heappop());
        
        self.data = temp;               # Restores back the heaplist.

        return ans;

    def parent(self, i):
        # Returns the parent of index i.
        return (i-1)//2;

    def children(self, i):
        # Returns the children indexes of index i.
        return (i<<1) + 1, (i<<1) + 2 ;
    
    def move_up(self, i_start):
        i = i_start;
        i_parent = self.parent(i);

        if i <= 0:      return;

        if self.data[i] < self.data[i_parent]:
            self.data[i], self.data[i_parent] = self.data[i_parent], self.data[i];
            self.move_up(i_parent);

        return;   

    def move_down(self, i_start = 0):
        i = i_start;
        max_size = len(self.data);

        if i >= max_size:     return;

        l, r    =   self.children(i);

        if r < max_size:

            if self.data[l] < self.data[r]:

                if self.data[l] < self.data[i]:
                    self.data[i], self.data[l] = self.data[l], self.data[i];
                    self.move_down(l);

            else:

                if self.data[r] < self.data[i]:
                    self.data[i], self.data[r] = self.data[r], self.data[i];
                    self.move_down(r);
            
        elif l < max_size:

            if self.data[l] < self.data[i]:
                self.data[i], self.data[l] = self.data[l], self.data[i];
                self.move_down(l);
        
        return;
    
    def heappop(self):
        
        if not self.data:           return None;
        elif len(self.data) == 1:   return self.data.pop();

        ans =   self.data[0];
        self.data[0] = self.data.pop();
        self.move_down();

        return ans;

    def heappush(self, x):
        
        self.data.append(x);
        self.move_up(len(self.data)-1);

class MaxHeap(MinHeap):

    def __init__(self, list_input = []):
        MinHeap.__init__(self, list_input);      

        return;
    
    def move_up(self, i_start):
        i = i_start;
        i_parent = self.parent(i);

        if i <= 0:      return;

        if self.data[i] > self.data[i_parent]:
            self.data[i], self.data[i_parent] = self.data[i_parent], self.data[i];
            self.move_up(i_parent);

        return;   

    def move_down(self, i_start = 0):
        i = i_start;
        max_size = len(self.data);

        if i >= max_size:     return;

        l, r    =   self.children(i);

        if r < max_size:

            if self.data[l] > self.data[r]:

                if self.data[l] > self.data[i]:
                    self.data[i], self.data[l] = self.data[l], self.data[i];
                    self.move_down(l);

            else:

                if self.data[r] > self.data[i]:
                    self.data[i], self.data[r] = self.data[r], self.data[i];
                    self.move_down(r);
            
        elif l < max_size:

            if self.data[l] > self.data[i]:
                self.data[i], self.data[l] = self.data[l], self.data[i];
                self.move_down(l);
        
        return;

