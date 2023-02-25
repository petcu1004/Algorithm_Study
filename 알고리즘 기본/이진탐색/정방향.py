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


arr = [4, 1, 5, 2, 3]
arr.sort()
result_index=binary_search(arr, 1)
print(result_index)
