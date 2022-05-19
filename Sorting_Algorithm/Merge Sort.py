# Merge sorting Algorithm.
def merge_sort(arr):
    if len(arr) > 1:   # Base case
        mid_elt = len(arr) // 2
        left_arr = arr[: mid_elt]
        right_arr = arr[mid_elt:]
# Recursion
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = 0
        j = 0
        k = 0
# Merging
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1
# Incase any value is left out  in the
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
arr = [1, 3, 5, 4, 2, 7, 8, 6]

merge_sort(arr)
print(arr)