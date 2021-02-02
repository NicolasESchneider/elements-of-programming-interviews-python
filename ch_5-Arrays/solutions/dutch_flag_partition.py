def dutch_flag_partition(array, pivot_idx):
    pivot = array[pivot_idx]
    smaller, equal, larger = 0, 0, len(array)
    while equal < larger:
        if array[equal] < pivot:
            array[smaller], array[equal] = array[equal], array[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif array[equal] == pivot:
            equal += 1
        else: # array[equal] > pivot
            larger -= 1
            array[equal], array[larger] = array[larger], array[equal]