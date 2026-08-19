numbers = [10, 20, 30, 40, 50]

search = int(input("Enter element to search: "))

found = False

for num in numbers:
    if num == search:
        found = True

if found:
    print("Element found")
else:
    print("Element not found")