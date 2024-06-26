def find_max_sum_sub_array(k, arr):
    max_sum = 0
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead

    return max_sum

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2]))  # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5]))  # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1]))  # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1]))  # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1]))  # 8
