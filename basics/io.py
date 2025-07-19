# get the input
name = input("Give me your name: ")
print("Huh, So you are", name)

"""
The input is a string hence needs to be converted
to an integer
"""
num1, num2 = input("Enter two numbers: ").split()
num1 = int(num1)
num2 = int(num2)

print("Product of the two: ", num1 * num2)
print("Sum of the two: ", num1 + num2)
print("Subract the two: ", num1 - num2)
print("Divide the two: ", num1 / num2)

# Output formatting
# ------
amount = 150.74
print("Amount: ${:.2f}".format(amount))

# Separator and End parameter
print("Python", end='@')
print('\n','G', 'F','G', sep='')

# f-string
print(f"Hi I am, {name}")

# Operator
print("The number is %d" %num1)