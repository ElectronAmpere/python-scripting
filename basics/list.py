# List (mutable data structure)
"""
Note:
5j+10 will be displayed as 10+5j
"""
list1=["geeks","for","geeks",100,10.19,5j+10,]
print("List1 ", list1)

list1=["geeks","for","geeks",100,10.19,10+5j,]
print("List1 ", list1)

# Indexed
print("List1[0]", list1[0])

# Ranges
print("Ranges of list", list1[0:4])

# list Backwards
print("Backward in list", list1[::-1])