# Python3 have dynamic data type
print("Base arithmetic expressions:")
x = 5
print(x)
x = "Hello!"
print(x)

# How to know type of variables cause of dynamic type issues
print("How to know type of variables cause of dynamic type issues:")
x = "Hello!"
type_of_variable = type(x)
print(type_of_variable)
x = 7
type_of_variable = type(x)
print(type_of_variable)
x = 5.6
type_of_variable = type(x)
print(type_of_variable)

# Arithmetic operations within variables
print("Arithmetic operations within variables:")
x = 5
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x ** y)
print(x / y)
print(x // y)
print(x % y)

# Example of variable naming: sum of loan rate example
print("Example of variable naming: sum of loan rate example")
loan = 1000
loan_rate = 10
number_of_years = 5
final_sum = loan + loan / 100 * loan_rate * number_of_years
print("Loan amount:", loan)
print("Loan rate:", loan_rate)
print("Number of years:", number_of_years)
print("Final sum of loan rate for number of years:", final_sum)