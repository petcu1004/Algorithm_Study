def binary_search(arr, value):
    left, right =0, len(arr)-1

    while left <= right:
        mid = (left+right) //2
        if arr[mid] == value:
            return mid
        if arr[mid] > value:
            right = mid -1
        else:
            left = mid +1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_index=binary_search(arr, 3)
print(result_index, arr[result_index])
