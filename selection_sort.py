import time


n = int(input("Enter number of elements: "))


arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))


start = time.time()


for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

   
    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

end = time.time()

print("Sorted Array:")
for i in arr:
    print(i, end=" ")

print("\nExecution Time:", end - start, "seconds")

print("\nTime Complexity:")
print("Best Case   : O(n²)")
print("Average Case: O(n²)")
print("Worst Case  : O(n²)")
print("Space Complexity: O(1)")
