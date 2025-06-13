list = [7, 20, 15, 3, 14, 12, 13, 5, 2, 0, 19]
print("first list:", list)

sum = 0

for i in list:
    sum += i

# to find average
avg = sum/len(list)

print("The sum of this list is:", sum)
print("The average is:", avg)

list.sort()

# to print the smallest and largest value in the list
print("The smallest value in this list is:", list[0])
print("The largest value in this list is:", list[-1])
