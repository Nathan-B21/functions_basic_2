# countdown
def countDown(num):
    new_list = []
    for i in range(num,-1,-1):
        new_list.append(i)
    return new_list

print(countDown(5))

# Print and Return
# Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(lst):
    print(lst[0])
    return lst[1]
print(print_and_return([1,2]))

# first Plus Length
# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length
def first_plus_length(lst):
    return lst[0] + len(lst)

print(first_plus_length([1,2,3,4,5]))

# This length, that value
# Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value
def length_and_value(size,val):
    my_list = []
    for i in range(0, size, 1):
        my_list.append(i)
        my_list[i] = val
    return my_list

print(length_and_value(4,7))
print(length_and_value(6,2))


