# Selection sort
"""
The process starts by finding the smallest value in the sequence and swaps it with the value in the first position of the sequence.
The second smallest value is then found and swapped with the value in the second position. This process contiunues positioning each successive value by selecting them from those not
yet sorted and swapping with the values with the respective positions.
It works in a fashion similar to what a human may use to sort a list of values.
The selection sort, which makes n-1 passes over the array to reposition n-1 values, is also O(n^2). 
THE DIFFERENCE between the selction and bubble sort is that the selection sort reduces the number of steps required to sort the list to O(n)
"""
# Algorithm
# Sorts a sequnce in ascending order using the selection sort algorithm.
def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n -1 ):
        smallestValIndex = i
        # determine if any other element contains a smaller value.
        for j in range(i + 1, n):
            if theSeq[j] < theSeq[smallestValIndex]:
                smallestValIndex = j
        # Swaps the ith value and smallValIndex only if the smallest value is not already in its proper position.
        if smallestValIndex != i:
            temp = theSeq[i]
            theSeq[i] = theSeq[smallestValIndex]
            theSeq[smallestValIndex] = temp

theSeq = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

print(theSeq)
selectionSort(theSeq)
print(theSeq)

# >> [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
# >> [2, 4, 5, 10, 13, 18, 23, 31, 51, 64, 29]