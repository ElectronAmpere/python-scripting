"""
Datatypes
-----

Numeric - int, float, complex
Sequence Type - string, list, tuple
Mapping Type - dict
Boolean - bool
Set Type - set, frozenset
Binary Types - bytes, bytearray, memoryview
"""
# Numeric (all are treated as a class)
a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))

# Sequences
s = 'Welcome to the Geeks World'
print(s)

# check data type (unicode)
print(type(s))

# access string with index
print(s[1])
print(s[2])
print(s[-1])

# Empty list (signed indexing - treated as direction)
a = []

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed int and string
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)

# initiate empty tuple
tup1 = ()
'''
Note  - The creation of a Python 
tuple without the use of parentheses is known as Tuple Packing. 
'''
tup2 = ('Geeks', 'For')
print("\nTuple with the use of String: ", tup2)

# Either this: tuple([1, 2, 3, 4, 5]) or below
tup1 = tuple((1, 2, 3, 4, 5))

# access tuple items
print(tup1[0])
print(tup1[-1])
print(tup1[-3])

# Boolean
print(type(True))
print(type(False))

# initializing empty set
s1 = set()

# Considers each character as individual element
s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)

set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# loop through set
for i in set1:
    print(i, end=" ")
    
# check if item exist in set    
print("Geeks" in set1)


"""
Values in a dictionary can be of any datatype and can be 
duplicated, whereas keys can’t be repeated and must be immutable. The dictionary can also be created by the built-in function dict().

Note  - Dictionary keys are case sensitive, the same name 
but different cases of Key will be treated distinctly. 
"""
# initialize empty dictionary
d = {}


d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)