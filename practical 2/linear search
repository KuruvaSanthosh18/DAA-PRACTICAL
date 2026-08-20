import time

n = int(input("Enter number of elements: "))


arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))


key = int(input("Enter the element to search: "))


start = time.time()


position = -1
for i in range(n):
    if arr[i] == key:
        position = i
        break


end = time.time()

if position != -1:
    print("Element found at position:", position + 1)
else:
    print("Element not found")

print("Execution Time:", end - start, "seconds")

print("\nTime Complexity:")
print("Best Case   : O(1)")
print("Average Case: O(n)")
print("Worst Case  : O(n)")
print("Space Complexity: O(1)")
