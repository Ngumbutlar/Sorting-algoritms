
def insertion_sort(arr):
    for i in range(1, len(arr)-1) :
        current = arr[i]
        j = i
        while arr[j-1] > current and j >0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j-=1



arr = [1, 3, 4, 2, 5]

insertion_sort(arr)
print(arr)
