## main_heapqueue.py

## Main function to test MinHeap and MaxHeap.
from random import randint;
from heap_queue import *;

DISPLAY_CHECKER  =   1;

def main():

    arr_len =   30;
    randoms =   [ randint(0, arr_len) for _ in range(arr_len)];


    min_heapq   =   MinHeap(randoms.copy());
    max_heapq   =   MaxHeap(randoms.copy());


    print("\n" +    "Min HEAP:    ", min_heapq.data);
    print(          "Max HEAP:    ", max_heapq.data, "\n");



    if DISPLAY_CHECKER:
        print("Python Sort: ", sorted(randoms));
        print("MinHeap Sort:", min_heapq.sorted());
        print("MaxHeap Sort:", max_heapq.sorted());

    sorted_randoms = sorted(randoms);
    assert  sorted_randoms          == min_heapq.sorted(), ' Min HEAP RESULT DOESN\'T MATCH';
    assert  sorted_randoms[::-1]    == max_heapq.sorted(), ' Max HEAP RESULT DOESN\'T MATCH';

    return 0;


if __name__ == '__main__':
    main();