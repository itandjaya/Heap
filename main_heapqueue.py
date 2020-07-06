## main_heapqueue.py

## Main function to test MinHeap and MaxHeap.
from random import randint;
from heap_queue import *;
from median import *;
from statistics import median as s_median;

DISPLAY_CHECKER  =   1;

def main():

    arr_len =   30;
    randoms =   [ randint(0, arr_len) for _ in range(arr_len)];


    min_heapq   =   MinHeap(randoms);
    max_heapq   =   MaxHeap(randoms);


    print("\n" +    "Min HEAP:    ", min_heapq.data);
    print(          "Max HEAP:    ", max_heapq.data, "\n");



    if DISPLAY_CHECKER:
        print("Python Sort: ", sorted(randoms));
        print("MinHeap Sort:", min_heapq.sorted());
        print("MaxHeap Sort:", max_heapq.sorted());

    sorted_randoms = sorted(randoms);
    assert  sorted_randoms          == min_heapq.sorted(), ' Min HEAP RESULT DOESN\'T MATCH';
    assert  sorted_randoms[::-1]    == max_heapq.sorted(), ' Max HEAP RESULT DOESN\'T MATCH';

    ## Testing MinHeap and MaxHeap to implement median.

    ## TESTING Median implementation using MinHeap and MaxHeap.

    m    =    Median([1,3,5,2]);
    #print(m.median(), m.max_heap.data, m.min_heap.data);
    assert m.add_value(10) == s_median(m.max_heap.data+ m.min_heap.data), 'Median Mismatch';
    assert m.add_value(3)== s_median(m.max_heap.data+ m.min_heap.data), 'Median Mismatch';
    assert m.add_value(20)== s_median(m.max_heap.data+ m.min_heap.data), 'Median Mismatch';
    assert m.add_value(7) == s_median(m.max_heap.data+ m.min_heap.data), 'Median Mismatch';
    assert m.add_value(23)== s_median(m.max_heap.data+ m.min_heap.data), 'Median Mismatch';
    assert m.add_value(8)== s_median(m.max_heap.data+ m.min_heap.data), 'Median Mismatch';
    assert m.add_value(14)== s_median(m.max_heap.data+ m.min_heap.data), 'Median Mismatch';
    assert m.add_value(10)==s_median(m.max_heap.data+ m.min_heap.data), 'Median Mismatch';
    assert m.add_value(11)==s_median(m.max_heap.data+ m.min_heap.data), 'Median Mismatch';
    assert m.add_value(22)==s_median(m.max_heap.data+ m.min_heap.data), 'Median Mismatch';

    return 0;


if __name__ == '__main__':
    main();