# Insertion Sort
"""
When implementing an insertion sort in a program, the algorithm maintains both the sorted and unsorted collections within the same sequence structure.
The algorithm keeps the list of sorted value at the front of the sequence and picks the next unsorted value from the first of those yet to be positioned.
To psotion the next item, the correct spot within the sequence of sorted values is found by performing a search. After finding the proper position,
the slot has to be opened by shifting the items down one position.
Here is my implementation of the inseriton sort algorithm in Python:
"""

# Sorts a sequnce in asceding order using the insertion sort algorithm.
def insertionSort(theSeq):
    n = len(theSeq)

    # starts with the first item as the only sorted entry
    for i in range(1, n):
        # Save the value to be positioned
        value = theSeq[i]
        # find the position where value fits in the ordered part of the list
        pos = i
        while pos > 0 and value < theSeq[pos-1]:
            # shift the items to the right during the search
            theSeq[pos] = theSeq[pos-1]
            pos -= 1

        # put the saved value into the open slot
        theSeq[pos] = value

theSeq = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29, 2, 18, 4, 31, 13, 5, 23, 64, 29]

print(theSeq)
insertionSort(theSeq)
print(theSeq)