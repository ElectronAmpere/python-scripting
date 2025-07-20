# A function
def hello():
    print("hello")

# Function call
hello()

def getInteger():
    return int(input("Enter an Integer: "))

def returnSomething(number: int) -> str:
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Default Arguments
"""
But once we have a default argument, all the arguments to 
its right must also have default values.
"""
def fun(x, y=20):
    print("x: ", x , "y: ", y)

# Positional Arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

# Arbitrary Arguments (* is the key identifier)
# The variable name starting with (*) is taken
# as variable argument
def variableArgs(*args):
    for arg in args:
        print(arg)
# Arbitrary Keyword Arguments (** is the key identifier)
# The variable name starting with (**) is taken
# as variable keyword argument
def variableKeyArgs(**kwargs):
    # Docstring
    """ Function to print the variable keyword arguments """
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

# Function with-in functions
def f1():
    s = 'I love GeeksforGeeks'
    
    def f2():
        print(s)
        
    f2()

# Anonymous functions (lambda functions)
def cube(x): return x*x*x # normal function
cube_l = lambda x : x*x*x # lambda function

# Pass by reference and Pass by value
# Here x is a new reference to same list lst
def byReference(x):
    x[0] = 20

# When we pass a reference and change the received 
# reference to something else, the connection between 
# the passed and received parameters is broken
def byValue(x):
    x = [20, 232,23]

def swap(x, y):
    temp = x
    x = y
    y = temp


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def Main():
    print("Main Started")

    # calling the function and storing the variable
    fun(returnSomething(getInteger()))

    print("Case-1:")
    nameAge("Suraj", 27)

    print("\nCase-2:")
    nameAge(27, "Suraj")
    variableArgs('Hello', 'Welcome', 'to', 'GeeksforGeeks')
    variableKeyArgs(first='Geeks', mid='for', last='Geeks')
    print(variableKeyArgs.__doc__)
    f1()
    print(cube_l(2))

    # Driver Code (Note that lst is modified
    # after function call.
    lst = [10, 11, 12, 13, 14, 15]
    print(lst)
    byReference(lst)
    print(lst)
    byValue(lst)
    print(lst)

    x = 2
    y = 3
    swap(x, y)
    print(x)
    print(y)
    print(factorial(4))


if __name__ == "__main__":
    Main()
    