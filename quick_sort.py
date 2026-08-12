def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

print("Original array:", arr)

sorted_arr = quick_sort(arr)

print("Sorted array:", sorted_arr)

print("Time Complexity:")
print("Best Case: O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case: O(n^2)")

print("Space Complexity: O(n log n)")
