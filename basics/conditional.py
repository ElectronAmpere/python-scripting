# Conditional Statement
# Get a number 
number = int(input("Enter a number: "))
if number > 29: print("Older")
elif number < 29: print("Younger")
else: print("Same age")

# Short hand (Ternary Operator)
result = "Younger" if number < 29 else "Older"
print("Result", result)


age = number

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

age = number
is_member = True if input("Are you a member? ") == "Yes" else False

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

match number:
    case 1 if number < 29:
        print("Younger")
    case 2 if number > 29:
        print("Older")
    case 3 if number == 29:
        print("Same age")
    case 4 | 5:
        print("Two or Three")
    case _:
        print("Other number")