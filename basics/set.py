"""
Set is a unordered, iterable, 
mutable collection without duplicates
The position of individual items are seemingly random
"""

myset = set(['Geeks', 'for', 'Geeks'])

"""
The set will be displayed alphabetically without
duplicates
"""
print(myset)

# union (combine two sets) 
myset = myset.union({'is', 'good'})
print(myset)
myset = myset.union({'star', 'platnium'})
print(myset)

# intersection (common in both the set)
set1 = {'can', 'you', 'dig', 'it'}
set2 = {'suck', 'ah', 'booker T', 'you'}
new_set = set1.intersection(set2)
print(new_set)