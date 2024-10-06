def sum_of_elements(numbers):
    #6Use the built-in sum() function to calculate the total sum of the list
    return sum(numbers)

#List of numbers
numbers = list(map(float, input("Enter the numbers : ").split()))

#Calculate the sum of elements
total_sum = sum_of_elements(numbers)

#Sum of the elements
print(f"The sum of the elements in the list is: {total_sum}")
