# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

# 2. Print the difference between the largest and smallest value:
# numbers.sort()
# diff_first_last = numbers[-1] - numbers[0]
# print(diff_first_last)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
last_number = 0
print(numbers)
for i in numbers:
    if i == last_number and i == 2:
        print(True)
    last_number = i
    

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
print(numbers)
sum = 0
can_count = True
for i in numbers:
    if i == 6:
        can_count = False
    elif i == 7:
        can_count = True
    elif i != 6 and can_count == True:
        sum = sum + i


print(sum)



# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

print(numbers)
sum = 0
position = 0
for i in numbers:
    if position == 0:
        if i != 13:
            sum = sum + i
        position = position + 1
    elif i != 13 and numbers[position-1] != 13:
        sum = sum + i
        position = position + 1
    else:
        position = position + 1
        print(position)

print(sum)
    





