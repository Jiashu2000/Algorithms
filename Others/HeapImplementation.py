# Heap Implementation

'''
Implementation of a priority queue with following methods
    1. Insert(H, x): given item x, insert into priority queue H
    2. Find(H): returns the element with highest priority in queue H. priority is commonly
        defined either by the largest or smallest key value among elements.
    3. Delete(H): remove the element with the smallest or largest value in the priority queue

Given an element of index k:
    - left child index: 2*k+1
    - right child index: 2*k+2
    - parent index: k/2 (taking the floor)

heaps work by maintaining a partial order on the set of elements that is weaker than the sorted order
so it is efficient to manage, yet stronger than random order so the minimu element can be quickly identified.

Implementation of a MinHeap:
    - peek: returns the smallest key stored in constant time
    - add: insert an element in the heap in its appropriate location
    - poll: remove the smallest key stored in the heap

'''

from typing import List, Optional

import sys


class MinHeap:
    
    def __init__(self, nodes: List[int] = []) -> None:
        self.nodes = []
        for node in nodes:
            self.nodes.add(node)
    
    def __len__(self) -> int:
        return len(self.nodes)
    
    def __is_empty(self) -> bool:
        return len(self.nodes) == 0

    def __get_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1
    
    def __get_right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2
    
    def __get_parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def __has_left_child(self, parent_index: int) -> bool:
        return self.__get_left_child_index(parent_index) < len(self.nodes)
    
    def __has_right_child(self, parent_index: int) -> bool:
        return self.__get_right_child_index(parent_index) < len(self.nodes)
    
    def __has_parent(self, child_index: int) -> bool:
        return self.__get_parent_index(child_index) < len(self.nodes)

    def __right_child(self, index: int) -> Optional[int]:
        if not self.__has_right_child(index):
            return -sys.maxsize
        return self.nodes[self.__get_right_child_index(index)]
    
    def __left_child(self, index: int) -> Optional[int]:
        if not self.__has_left_child(index):
            return -sys.maxsize
        return self.nodes[self.__get_left_child_index(index)]
    
    def __parent(self, index: int) -> Optional[int]:
        if not self.__has_parent(index):
            return -sys.maxsize
        return self.nodes[self.__get_parent_index(index)]
    
    '''
    Inserting into the MinHeap
        1. add the incoming key by appending to the end
        2. heapify up newly-added element to its correct position
            - get the element
            - check if it disobeys the priority rule: check if the key value is smaller than the parent
            - if smaller, swap with its parent
            - recurse in the index of the parent
            - keeping bubbling up util reaching the root
    '''

    def __swap(self, first_idx: int, second_idx: int):
        if first_idx >= len(self.nodes) or second_idx >= len(self.nodes):
            print(f'first ({first_idx}) or second ({second_idx}) are invalid')
            return 
        tmp = self.nodes[first_idx]
        self.nodes[first_idx] = self.nodes[second_idx]
        self.nodes[second_idx] = tmp

    def __heapify_up(self, child: Optional[int] = None):
        '''move last added element to correct position in heap'''
        if not child:
            # start from the last
            child = len(self.nodes) - 1
        # check if it is smaller than the parent
        parent_idx = self.__get_parent_index(child)
        if self.__parent(child) and self.nodes[self.__parent(child)] < self.nodes[child]:
            self.__swap(parent_idx, child)
            self.__heapify_up(child = parent_idx)
        return self.nodes
    
    def add(self, item: int):
        self.nodes.append(item)
        self.__heapify_up()
    
    '''
    Deleting from the MinHeap 
        1. move the last element to the first position
        2. shrink the size down by 1 and heapify down
            - get the element key(start with the first key)
            - check if the key is greater than any child
            - if greater, swap with the smallest between left and right
            - continue heapify down with the smallest child index
            - repeat until no more child
    '''

    def __heapify_down(self, index: Optional[int] = 0):
        """move root to the proper position in heap"""
        # if it does not have left child, it must not have right child
        if index >= len(self.nodes) or not self.__has_left_child(index):
            return self.nodes
        
        # check if greater than left or right
        smaller_child_idx = self.__get_left_child_index(index)
        if self.__has_right_child(index) and \
            self.__right_child(index) < self.__left_child(index):
            smaller_child_idx = self.__get_right_child_index(index)
        
        if self.nodes[index] < self.nodes[smaller_child_idx]:
            # lower than both, do nothing
            return self.nodes
        
        if self.nodes[index] > self.nodes[smaller_child_idx]:
            self.__swap(index, smaller_child_idx)
            return self.__heapify_down(smaller_child_idx)
    
    def poll(self) -> Optional[List]:
        '''
        polls lowest element from the heap (the root)
        copy the last elment to the first position, shrink the size by 1 and heapify down
        '''
        
        if self.is_empty():
            print("Empty, no polling!")
            return None
        
        # remove first and insert the last one added as the root
        removed_node = self.nodes[0]
        self.nodes[0] = self.nodes[len(self.nodes) - 1]

        del self.nodes[-1]
        
        self.__heapify_down()
        return removed_node
    
    '''
    Peek
    the peek operation return the smallest key from the heap
    '''
    def peek(self) -> Optional[int]:
        if self.__is_empty():
            return None
        return self.nodes[0]

    def heapify_children(self, index: int):
        '''
        heapify children of a node to obey left < right
        '''
        if not self.__has_left_child(index):
            return
        if not self.__has_right_child(index):
            return
        if self.__right_child(index) < self.__left_child(index):
            self.__swap(
                self.__get_right_child_index(index),
                self.__get_left_child_index(index))
        self.heapify_children(self.__get_left_child_index(index))
        self.heapify_children(self.__get_right_child_index(index))
    
    '''
    Heapsort
    we add the unsorted elements to the heap and keep polling. 
    In each iteration of the polling loop, we are extracting the smallest key and re-organizing the heap.
    
    time complexity: o(n * logn)
    '''

    def heapsort_aux(unsorted_input: List[int]) -> List[int]:
        '''heapsort using o(n) space'''
        heap = MinHeap(unsorted_input)
        sorted_input = []
        for _ in range(len(unsorted_input)):
            sorted_input.append(heap.poll())
        
        # should return false
        print(f'identity check: {sorted_input is heap.nodes}')
        return sorted_input


    def heapsort_in_place(unsorted_input: List[int]) -> List[int]:
        '''heapsort in-place'''        
        heap = MinHeap()
        heap.nodes = unsorted_input
        size = len(unsorted_input)
        print(f'identity check: {heap.nodes is unsorted_input}')

        for idx in range(size//2, -1, -1):
            heap.__heapify_down(idx)
        heap.heapify_children(0)
        return heap.nodes


if __name__ == '__main__':
    unsorted_array = [10, 15, 8, 20, 17, 14, 13]
    print(f'heapsort in-place: {MinHeap.heapsort_in_place(unsorted_array)}')
    # identity check: True
    # heapsort with aux space: [8, 10, 15, 17, 20]
        

    