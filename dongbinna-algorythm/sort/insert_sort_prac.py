
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr






arr = [5,2,63,3,53,12,3,53,63,534,1,4,23]
print(insertion_sort(arr))