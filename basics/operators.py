num1, num2 = input("Enter two numbers: ").split()
num1 = int(num1)
num2 = int(num2)

print("Product of the two: ", num1 * num2)
print("Sum of the two: ", num1 + num2)
print("Subract the two: ", num1 - num2)
print("Divide the two: ", num1 / num2)
print("Floor Division: ", num1 // num2)
print("Modulus: ", num1 % num2)
print("Exponentiation: ", num1 ** num2)

# Comparison Outputs
print("Greater than", num1 > num2)
print("Less than", num1 < num2)
print("Equal to", num1 == num2)
print("Not Equal to", num1 != num2)
print("Greater than or equal to", num1 >= num2)
print("Less than or equal to", num1 <= num2)

# Logical Operators
a = True
b = False
print("And ", a and b)
print("Or ", a or b)
print("Not ", not b)


# Bitwise Operators
a = 0x10
b = 0x04

print(f"a = {hex(a)}, b = {hex(b)}")
print("a & b", a & b)
print("a | b", a | b)
print("~b", ~b)
print("a ^ b", a ^ b)
print("a >> 2", a >> 2)
print("a << 2", a << 2)

# Assignment Operators
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

# Identity Operators
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# Membership Operators
list = [10, 20, 30, 239, 92]
x =20
if x not in list:
    print('x is not in the list')
else:
    print()

y = 1
if y in list:
    print("y is in the list")
else:
    print("y is not in the list")

print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)