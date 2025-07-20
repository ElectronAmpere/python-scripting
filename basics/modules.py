# math module
import math


# factorial
def factorial(number):
    fact = 1
    for item in range(1, number + 1):
        fact *= item
    return fact

print(f"log of {factorial(5)} = {math.log(factorial(5), 2)}")