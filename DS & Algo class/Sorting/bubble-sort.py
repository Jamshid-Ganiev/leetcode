# Bubble Sort
"""
The outer loop is executed n-1 times since the algorithm makes n-1 passes over the sequence. The number of iterations for the inner loop is not fixed, but depends on the current iteration of the outer loop.
On the first pass over the sequence, the inner loop executes n01 times, on the second path, n-2 times, on the third, n-3 times, and so on until it executes once on the last pass. The total number of iterations
for the inner loop will be the sum of the first n-1 integers, which equals (n(n-1)/2) - 2 = 1/2n^2 + 1/2n , resulting in a run time of O(n^2).
Bubble sort is considered one of the most inefficient sorting algorithms due to the total number of swaps required.

But what if the sequence is already in sorted array?
: In this case, there would be no need to sort the sequence. But our implementation still performs all n^2 iterations because it has no way of knowing thw sequence is already sorted.
"""

# Algorithm
# Sorts a sequnce in an ascending order using the bubble sort algorithm
def bubbleSort(theSeq):
    n = len(theSeq) - 1
    # perform n bubble operations in the sequence
    for i in range(n):
        # bubble the largest value to the end
        for j in range(0, n-i):
            if theSeq[j] > theSeq[j+1]:
                temp = theSeq[j]
                theSeq[j] = theSeq[j+1]
                theSeq[j+1] = temp

theSeq = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

print(theSeq)
bubbleSort(theSeq)
print(theSeq)