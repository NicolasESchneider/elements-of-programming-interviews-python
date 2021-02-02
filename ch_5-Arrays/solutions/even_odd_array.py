def even_odd(array):
    next_even, next_odd = 0, len(array) - 1
    while next_even < next_odd:
        if array[next_even] % 2 == 0:
            next_even += 1
        else:
            array[next_even], array[next_odd] = array[next_odd], array[next_even]
            next_odd -= 1