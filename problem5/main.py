def remove_duplicates(array):
    if len(array) == 0:
        return 0

    next_non_duplicate = 1  # Pointer to the next position of non-duplicate element
    for i in range(1, len(array)):
        if array[next_non_duplicate - 1] != array[i]:
            array[next_non_duplicate] = array[i]
            next_non_duplicate += 1

    return next_non_duplicate

if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))  # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9]))  # 6
    print(remove_duplicates([2, 2, 2, 11]))  # 2
    print(remove_duplicates([2, 2, 2, 11]))  # 2
    print(remove_duplicates([1, 2, 3, 11, 11]))  # 4
