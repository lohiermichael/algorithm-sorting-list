# algorithm-sorting-list

This repository will gather different algorithms of list sorting.  It will highlight the performance of the **Divide to Conquer** paradigm in the context of the exercise of sorting a list.

## Introduction to the problem

This exercise is often the first exercise to approach the paradigm of **Divide to conquer** and has different solutions around this concept

### Input

Given a list of n integers: 
`L = [a1, ..., an]

### Goal 

We want to return the sorted list of L: 
`sorted_L = [a.s(1), .... a.s(n)]` so that  <br>
a.s(1) < a.s(2) < ... < a.s(n) 

## Solutions

### Insertion sort

This method consists of scanning through the elements from left to right <br>
For each iterated element of the list, while the element right before it, on its left is bigger than itself, you swap the position of these elements.

The strategy can be seen as a **brute force** approach. The complexity of this algorithm is **O(n2)** in average.

### Merge sort

This method follows the principle of **divide to conquer**.

#### 1. DIVIDE

We first split the list it two equal parts, both having "half" the size of the initial list

#### 2. CONQUER

We apply the sorting algorithm on both of these sub-lists: L_left and L_right

#### 3. COMBINE

That is the final step which merges L_left and L_right to build L_final <br>
We build the final list by iterating through L_left with i and L_right with j
While we have not scanned through both L_left and L_left:
* ***If L_left[i] <= L_right[j]:*** we append L_left[i] to L_final an increment i
* ***If L_left[i] > L_right[j]:*** we append L_right[j] to L_final an increment j.

This method has a complexity of **O(nln(n))** in average.

### Quick sort

This method follows the principle of **divide to conquer**.

#### 1. DIVIDE

We choose an element of the list that we pop from it. We call it **pivot**.
We scan through the remaining elements of the list and keep all the elements that are inferior to **pivot** on the left (L_left) and all those which are superior on the right (L_right)

#### 2. CONQUER

We apply the sorting algorithm on both of these sub-lists: L_left and L_right

#### 3. COMBINE

There is no need for a combining step

This method has a complexity of **O(nln(n))** in average.

***Note**: In the worst case scenario (i.e. when the list is reversely sorted, this algorithm is slow: complexity of **O(n2)** if we choose the pivot to be the first element (or any other fixed element) of the list at each step.*

An improvement of the algorithm is to choose the pivot as a randomized element of the list at each step. This then gives an average complexity of **O(nln(n))**. 
