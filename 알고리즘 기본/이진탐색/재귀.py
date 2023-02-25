def binarySearch(array, target, left, right):
    mid = (left+right) //2
    
    if target == array[mid]:
        print(mid)
        # return mid
    elif array[mid] > target:
        binarySearch(array, target, left, mid-1)
    else:
        binarySearch(array, target, mid+1, right)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr.sort()
binarySearch(arr, 3, 0, len(arr)-1)
