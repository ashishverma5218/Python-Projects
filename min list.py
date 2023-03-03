lis1 = []
total_element = int(input(" How many elements you want to enter? "))
for i in range(total_element):
    n = int(input("Enter a number:"))
    lis1.append(n)
print(lis1)
lis1.sort()
print("Minimum element is ",lis1[0])

