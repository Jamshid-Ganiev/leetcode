# Quick Sort Sorting algorithm is highly efficient sorting algorithm that divides a large data array into smaller ones. A vast array is divided into two
# sub arrays, one containing the values smaller than the pivot and one containing greater than the pivot. It uses the Divide & Conquer strategy, by creating the base case
# of returning array itself if the length of the array is 0 or 1.

# Algorithm

def quickSort(array):
    if len(array) < 2:
        return array  # Base Case
    else:
        pivot = array[0]
        
        # values less than the pivot
        less = [n for n in array[1:] if n <= pivot]

        # values greater than the pivot
        greater = [n for n in array[1:] if n > pivot]

        return quickSort(less) + [pivot] + quickSort(greater)
    
print(quickSort([345,346,2345,785,1245,123,342,34,876,54,34,2,246]))

# Result: 
# >>> [2, 34, 34, 54, 123, 246, 342, 345, 346, 785, 876, 1245, 2345]