import time


n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))


start = time.time()


for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key


end = time.time()


print("\nSorted Array:")
print(arr)

print("Execution Time:", end - start, "seconds")


print("\nTime Complexity:")
print("Best Case   : O(n)")
print("Average Case: O(n^2)")
print("Worst Case  : O(n^2)")
print("Space Complexity: O(1)")
