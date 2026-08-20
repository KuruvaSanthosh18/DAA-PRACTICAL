import time

n = int(input("Enter number of elements: "))


arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

start = time.time()


for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp


end = time.time()


print("Sorted Array:")
for i in arr:
    print(i, end=" ")

print("\nExecution Time:", end - start, "seconds")

print("\nTime Complexity:")
print("Best Case   : O(n^2)")
print("Average Case: O(n^2)")
print("Worst Case  : O(n^2)")
print("Space Complexity: O(1)")
